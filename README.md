# nwdiag on heroku

It runs [nwdiag](http://blockdiag.com/en/nwdiag/index.html) on [heroku](https://www.heroku.com/).

# API

A REST API is provided.
You can use the api like below.

```
$ curl -X POST -H "Content-Type: application/json" "https://nwdiag.herokuapp.com/" -d '<nwdiag data>' > diagram.svg
```

``<nwdiag data>`` is json data like below. see [nwdiag](http://blockdiag.com/en/nwdiag/index.html).

```
nwdiag {
  network dmz {
      address = "210.x.x.x/24"

      web01 [address = "210.x.x.1"];
      web02 [address = "210.x.x.2"];
  }
  network internal {
      address = "172.x.x.x/24";

      web01 [address = "172.x.x.1"];
      web02 [address = "172.x.x.2"];
      db01;
      db02;
  }
}
```

## Parameters

* imagetype
  * svg (default)
  * png
* width
* height

## Examples

Here are some examples.

```
$ curl -X POST -H "Content-Type: application/json" "https://nwdiag.herokuapp.com/?width=1280&height=1024" -d '<nwdiag data>' > diagram.svg
$ curl -X POST -H "Content-Type: application/json" "https://nwdiag.herokuapp.com/?imagetype=png" -d @sample.json > diagram.png
```
