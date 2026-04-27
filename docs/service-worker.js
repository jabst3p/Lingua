const CACHE = "moti-cache-v1";

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE).then(cache =>
      cache.addAll([
        "./index.html",
        "./styles.css",
        "./app.js",
        "./manifest.webmanifest",
        "./data/wiktionary.json",
        "./data/webster1913.json",
        "./data/etymonline.json",
        "./data/idioms.json",
        "./data/collocations.json",
        "./data/examples.json"
      ])
    )
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(res => res || fetch(event.request))
  );
});
