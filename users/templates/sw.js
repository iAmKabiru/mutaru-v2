this.addEventListener('install',(event)=>{
    console.log("SW installed");
    event.waitUntil(
        caches.open('static')
        .then((cache)=>{
            cache.addAll([
                '/',
                 '../../project/templates/project/project_list.html',
                '/main.js',
                '/bootstrap.min.js',
                '/jquery.min.js',
                '/base.css',
                '/bootstrap.min.css',
                '/fontawesome.css',
                '/img/splash.png',
                '/img/logo.png',
            ]);
        })
    );
});
this.addEventListener('activate',()=>{
    console.log("SW Activated");
    caches.keys()
        .then(names=>{
            names.forEach(name=>{
                caches.delete(name);
            })
        })
});

this.addEventListener('fetch',(event)=>{
    event.respondWith(
        caches.match(event.request)
         .then((res)=>{
             if(res) return res;
             else return fetch(event.request);
         })
    );
});