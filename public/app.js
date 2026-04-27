// ------------------------------
// AUTO-LOAD ALL JSON FILES
// ------------------------------

const DATA_FILES = [
  "wiktionary.json",
  "webster1913.json",
  "etymonline.json",
  "idioms.json",
  "collocations.json",
  "examples.json"
];

const SOURCES = {
  wiktionary: "Wiktionary",
  webster1913: "Webster 1913",
  etymonline: "Etymonline",
  idioms: "Idioms",
  collocations: "Collocations",
  examples: "Flavorful Examples"
};

let index = new Map(); // headword → { source → entries }
let currentWord = null;

// ------------------------------
// LOAD ALL DATA
// ------------------------------

async function loadAll() {
  for (const file of DATA_FILES) {
    const id = file.replace(".json", "");
    const res = await fetch("data/" + file);
    const raw = await res.json();
    normalize(id, raw);
  }
}

function normalize(source, raw) {
  raw.forEach(entry => {
    const head = (entry.headword || entry.word || "").toLowerCase();
    if (!head) return;

    if (!index.has(head)) index.set(head, {});
    if (!index.get(head)[source]) index.get(head)[source] = [];

    index.get(head)[source].push(entry);
  });
}

// ------------------------------
// FUZZY SEARCH
// ------------------------------

function levenshtein(a, b) {
  const dp = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    let prev = dp[0];
    dp[0] = i;
    for (let j = 1; j <= b.length; j++) {
      const tmp = dp[j];
      dp[j] = a[i - 1] === b[j - 1]
        ? prev
        : Math.min(prev + 1, dp[j] + 1, dp[j - 1] + 1);
      prev = tmp;
    }
  }
  return dp[b.length];
}

function fuzzyScore(word, query) {
  const w = word.toLowerCase();
  const q = query.toLowerCase();
  if (w.startsWith(q)) return 0;
  if (w.includes(q)) return 1;
  return levenshtein(w, q);
}

// ------------------------------
// RENDER SEARCH RESULTS
// ------------------------------

const resultsEl = document.getElementById("results");
const searchEl = document.getElementById("search");

searchEl.oninput = () => {
  const q = searchEl.value.trim().toLowerCase();
  if (!q) {
    resultsEl.innerHTML = "";
    return;
  }

  const scored = [];
  for (const [head] of index.entries()) {
    const score = fuzzyScore(head, q);
    if (score <= 3) scored.push({ head, score });
  }

  scored.sort((a, b) => a.score - b.score);

  resultsEl.innerHTML = "";
  scored.slice(0, 200).forEach(({ head }) => {
    const li = document.createElement("li");
    li.textContent = head;
    li.onclick = () => showEntry(head);
    resultsEl.appendChild(li);
  });
};

// ------------------------------
// SHOW ENTRY
// ------------------------------

const titleEl = document.getElementById("word-title");
const metaEl = document.getElementById("word-meta");
const defEl = document.getElementById("definition");
const saveBtn = document.getElementById("save-btn");

function showEntry(head) {
  currentWord = head;
  const data = index.get(head);

  titleEl.textContent = head;
  metaEl.textContent = Object.keys(data)
    .map(s => SOURCES[s] || s)
    .join(" · ");

  const blocks = [];

  for (const source in data) {
    const label = SOURCES[source] || source;
    const entries = data[source];

    let html = `<div class="source-block">
      <div class="source-label">${label}</div>`;

    entries.forEach(e => {
      if (source === "etymonline") {
        html += `<div class="etym">${escapeHtml(e.etymology || e.text || "")}</div>`;
      } else if (source === "idioms") {
        e.idioms?.forEach(i => {
          html += `<div>${escapeHtml(i.phrase)} — ${escapeHtml(i.meaning)}</div>`;
        });
      } else if (source === "collocations") {
        if (e.collocates?.adjectives)
          html += `<div>Adjectives: ${e.collocates.adjectives.join(", ")}</div>`;
        if (e.collocates?.verbs)
          html += `<div>Verbs: ${e.collocates.verbs.join(", ")}</div>`;
      } else if (source === "examples") {
        e.examples?.forEach(ex => {
          html += `<div>• ${escapeHtml(ex)}</div>`;
        });
      } else {
        const defs = e.definitions || [];
        defs.forEach(d => {
          html += `<div>${escapeHtml(d)}</div>`;
        });
      }
    });

    html += `</div>`;
    blocks.push(html);
  }

  defEl.innerHTML = blocks.join("");
  saveBtn.disabled = false;
}

// ------------------------------
// MULTIPLE NAMED LISTS
// ------------------------------

const LISTS_KEY = "moti-lists";

function loadLists() {
  return JSON.parse(localStorage.getItem(LISTS_KEY) || "{}");
}

function saveLists(lists) {
  localStorage.setItem(LISTS_KEY, JSON.stringify(lists));
}

function addToList(name, word) {
  const lists = loadLists();
  if (!lists[name]) lists[name] = [];
  if (!lists[name].includes(word)) lists[name].push(word);
  saveLists(lists);
}

saveBtn.onclick = () => {
  const name = prompt("Add to which list?");
  if (name) addToList(name, currentWord);
};

// ------------------------------
// LISTS VIEW
// ------------------------------

const tabBrowse = document.getElementById("tab-browse");
const tabLists = document.getElementById("tab-lists");
const viewBrowse = document.getElementById("view-browse");
const viewLists = document.getElementById("view-lists");
const listsEl = document.getElementById("lists");
const listTitleEl = document.getElementById("list-title");
const listWordsEl = document.getElementById("list-words");
const newListBtn = document.getElementById("new-list-btn");

tabBrowse.onclick = () => {
  tabBrowse.classList.add("active");
  tabLists.classList.remove("active");
  viewBrowse.classList.remove("hidden");
  viewLists.classList.add("hidden");
};

tabLists.onclick = () => {
  tabLists.classList.add("active");
  tabBrowse.classList.remove("active");
  viewLists.classList.remove("hidden");
  viewBrowse.classList.add("hidden");
  renderLists();
};

newListBtn.onclick = () => {
  const name = prompt("New list name:");
  if (!name) return;
  const lists = loadLists();
  lists[name] = lists[name] || [];
  saveLists(lists);
  renderLists();
};

function renderLists() {
  const lists = loadLists();
  listsEl.innerHTML = "";
  listTitleEl.textContent = "";
  listWordsEl.innerHTML = "";

  Object.keys(lists).forEach(name => {
    const li = document.createElement("li");
    li.textContent = `${name} (${lists[name].length})`;
    li.onclick = () => showList(name);
    listsEl.appendChild(li);
  });
}

function showList(name) {
  const lists = loadLists();
  const words = lists[name] || [];
  listTitleEl.textContent = name;
  listWordsEl.innerHTML = "";

  words.forEach(w => {
    const li = document.createElement("li");
    li.textContent = w;
    li.onclick = () => {
      tabBrowse.onclick();
      showEntry(w);
    };
    listWordsEl.appendChild(li);
  });
}

// ------------------------------
// UTILS
// ------------------------------

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

// ------------------------------
// INIT
// ------------------------------

loadAll();
