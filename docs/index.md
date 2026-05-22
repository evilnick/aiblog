# My AI pick of the month

There are many AI tools which concentrate on specifics, such as image generation, 3D models or writing code, which seem to get all the attention. There are plenty of specialist AI tools which get less attention but which are, in their own way, just as useful. Here I want to briefly introduce one of them: LibreTranslate.

The world has a rich diversity of languages, and it is always more comforting to read instructions, comments and explanations in one you are most familiar with. There are a number of translation implementations, probably the best known of which is Google Translate (there are actually several variations of the API), but I frequently find myself using LibreTranslate for tasks like translating emails, deciphering Chinese technical specs or generating static text for user interfaces. 

Here are some good reasons to opt for LibreTranslate:

- Free and open source
- Can run self-hosted / air-gapped / IoT
- Works with a simple REST API 
- Trainable on your own data

## Try it yourself

Self-hosted sounds like a lot of effort, but in reality, it just takes a couple of steps. The recommended way (for all platforms) is to use the official Docker image. This is definitely the right choice if you want to use this as a permanent service (you should check out the [official documentation](https://docs.libretranslate.com/guides/installation/) for the various ways to set up and configure it). However, if you are already working with Python and want to try it out you can just use `pip`:

```
pip install libretranslate
```
Then run the server:

```
libretranslate --load-only en,de,fr,zh
```
If you omit the language arguments, LibreTranslate will download all the languages it knows (currently around 30) which will take some extra time.

!!! note
    If you run into compiler errors when installing with pip, use the Docker image instead, which bypasses local dependency problems entirely.

By default LibreTranslate will run a service on the local host at port 5000. It also includes a simple web frontend you can use to check that it's running: <http://localhost:5000/>

## Using it with Python

There is a specific Python package for working with LibreTranslate ([libretranslatepy](https://github.com/argosopentech/LibreTranslate-py)), but actually the API is easy to use with standard requests so it isn't really necessary to add extra dependencies. To translate a string, just construct a JSON payload and send it to the server. Here's an example in the interactive Python shell:

```
>>> import requests
>>> url = "http://localhost:5000/translate"
>>> mytext = "This is all very interesting"
>>> payload = { "q": mytext, "source": "en", "target": "de", "format": "text"}
>>> response = requests.post(url, json=payload)
>>> response.json()
{'translatedText': 'Das ist alles sehr interessant'}
```

The API can also handle automatic language detection and deal with examples embedded in markup like HTML. There are more examples in the [LibreTranslate API documentation](https://docs.libretranslate.com/guides/api_usage/).


## Using it with caution

AI translation is a great enabler, but as with all AI, it isn't perfect. For translation in particular, AI hallucinations lead to grammatically correct and convincing text which doesn't capture the intent of the original. 

For example, although larger models can handle idioms well, smaller models often fail. Consider the French ***"Tu vas lui poser un lapin?"***. LibreTranslate will return ***"Are you gonna put a rabbit on them?"*** which, while the use of "gonna" tries to capture informal language, fails to spot that "putting a rabbit" on someone is a common French idiom for "standing them up". If your sources are free of idiomatic language, you'll get much better results!


