# AI translation using LibreTranslate

In addition to general AI models, some specialise in a particular area such as image generation or writing code. Translation is an often overlooked area where the use of AI is practical and efficient for developers. Google Translate in various different forms is best known of these, but LibreTranslate is a free and open-source alternative which has some advantages for developers:

- Free and open source
- Can run self-hosted / air-gapped / IoT
- Works with a simple REST API 
- Trainable on your own data

By the end of this short tutorial you will be able to run a LibreTranslate service locally and use a Python script to translate strings into more than 30 different languages using its REST API.

## 1. Install and Run the LibreTranslate Server

Self-hosting services can often seem like a lot of effort, but LibreTranslate just takes a couple of steps. The recommended way (for all platforms) is to use the official Docker image. This is definitely the right choice if you want to use this as a permanent service (see the [official documentation](https://docs.libretranslate.com/guides/installation/) for a number of ways to set up and manage it). However, if you are already working with Python and want to try it out you can just use `pip` to install it:

```
pip install libretranslate
```

!!! note
    If you run into compiler errors when installing with pip, use the Docker installation method instead, which bypasses local dependency problems entirely.

When running the server, you may wish to limit it to languages you are going to actually use, as loading each one takes some time and extra resources. Languages, identified by their [ISO 639 two-letter code](https://www.loc.gov/standards/iso639-2/php/code_list.php), can be supplied as an argument when starting the server. 

```
libretranslate --load-only en,de,fr,zh
```
In the above example the server will load English, German, French and Chinese.

By default LibreTranslate will run its service on the local host at port 5000. It also includes a simple web frontend you can use to check that it's running: <http://localhost:5000/>

## 2. Access the API With Python

There is a specific Python package for working with LibreTranslate,[libretranslatepy](https://github.com/argosopentech/LibreTranslate-py). However, the API is not extensive or complicated to use with standard requests so it isn't really necessary to add extra dependencies. To translate a string, just construct a JSON payload and send it to the server using the [`requests`](https://realpython.com/python-requests/) package. Here's an example script which constructs the required HTTP request from your input and prints out the received translation:

``` py title="translate_text.py"
import requests

url = "http://localhost:5000/translate"
mytext = input("Enter the text to translate: ")
payload = {"q": mytext,
           "source": "en",
           "target": "de",
           "format": "text"}         
response = requests.post(url, json=payload)

print( f"That translates to German as: {response.json()['translatedText']}")

```

Here's a quick explanation of what is being passed to the server in the payload described above:

| Argument     | Description                                          |
| ------------ | ---------------------------------------------------- |
| q            | the query text to be translated                      |
| source       | 2-letter source language code (can be set to 'auto') |
| target       | 2-letter target language code                        |
| format       | 'text' or 'html' for formatted markup text           |

The return values from the request are then stored in 'response' and output to the user. For a real application you would want to add checks to ensure that the response was valid.


## 3. Some Cautionary Advice

AI translation is a great enabler, but as with all AI, it isn't perfect. For translation in particular, AI hallucinations lead to grammatically correct and convincing text which doesn't capture the intent of the original. 

For example, although larger models can handle idioms well, smaller models often fail. Consider the French ***"Tu vas lui poser un lapin?"***. LibreTranslate will return ***"Are you gonna put a rabbit on them?"*** which, while the use of "gonna" tries to capture informal language, fails to spot that "putting a rabbit" on someone is a common French idiom for "standing them up". If your sources are free of idiomatic language, you'll get much better results.

Also bear in mind that this model is running on your own hardware - trying to translate large amounts of text is going to be much slower than a cloud-based API.


