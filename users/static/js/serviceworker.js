var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/',
        'css/base.css',
        'https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css',
        'main.js',
        'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
        'jquery.min.js',
        'bootstrap.min.js'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
