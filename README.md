# django-tatujs

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Integration of [TatuJS](https://github.com/sophilabs/tatujs) with Django.

## Installation
Run the included ```setup.py```.

## Configuration

### 1. Enable the middleware
Add ```tatujs.middleware.ExtractorMiddleware``` to your ```MIDDLEWARE_CLASSES``` setting in your django project.

### 2. Configure TatuJS

#### Example configuration:
```js
// The middleware included will look for this HTTP header.
tatu.configuration.headerName = 'X-Source'; // <= Sources header

tatu.configuration.extractor = 'silent';
tatu.configuration.reload = false;
tatu.configuration.targetSymbol = '>>';
tatu.configuration.concurrency = 42;

tatu.configuration.sources = {
  /*
   * Pages of the menu
   */
  '.navbar a': {
    'loader': 'html',

    'selectors': 'title,.container,.navbar',
    'handlers': 'title,outer,history,inspect,event',
    'cache': 'object',

    'sources': {
      'img': {
        'loader': 'image'
      },
      'video': {
        'loader': 'video',
        'minBuffered': 10
      }
    }
  },

  /*
   * Tabs inside Page 0
   */
  '.tatu-tabs a': {
    'loader': 'html',

    'selectors': 'title,.tatu-tab-content,.tatu-tabs',
    'handlers': 'title,outer,inspect,event',
    'cache': 'object'
  }
};
```

## Example
An example is included. Enable the middleware, add ```tatujs.demo``` to your ```INSTALLED_APPS```, and add the following to your main urlconf.

```
url(r'^demo/', include('tatujs.demo.urls')),
```

## License
django-tatujs is Copyright (c) 2017 sophilabs, inc. It is free software, and may be
redistributed under the terms specified in the [license](/LICENSE) file.

## About

[![sophilabs.co](https://s3.amazonaws.com/sophilabs-assets/logo/logo_300x66.gif)](https://sophilabs.co)

django-tatujs is maintained and funded by sophilabs, inc. The names and logos for
sophilabs are trademarks of sophilabs, inc.
