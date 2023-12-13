const cacheName = 'superapp-cache-v1';

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(cacheName)
      .then(cache => cache.addAll([
        '/',
        '/static/css/style.css',
        '/static/js/main.js',
        '/static/images/komo1.jpeg',
        // Ajoutez d'autres fichiers que vous souhaitez mettre en cache
      ]))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});