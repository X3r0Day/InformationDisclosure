

# InformationDisclosure

> Scrape the hidden

---

A tool to dig up the past for publicly available data... because why wait for secrets to come to you when you can just search for them?

---

## Feature

Uses `CDX` API of Web Archive to filter out files with **"Specific Keywords"**

You can find files which contains keyword "Confidential" if the file extension is under [`file_extensions.json`](https://github.com/X3r0Day/InformationDisclosure/blob/main/file_extensions.json)

---

## Installation

### Dependecy:

`colorama`
`python 3.8+`

### Installing:

```
git clone https://github.com/X3r0Day/InformationDisclosure.git
cd InformationDisclosure
python3 InformationDisclosure.py
```

---

## Configuration 

You can add custom file extension which you want to also include in scraped data in [`file_extensions.json`](https://github.com/X3r0Day/InformationDisclosure/blob/main/file_extensions.json)


---

## How Does It Work?

It uses `CDX` api of [Web Archive](http://web.archive.org/) to filter out unnecessary files.

---

## **Disclaimer:**

#### This tool is for educational/research purposes only. Use it responsibly and don’t break the internet. I’m not responsible for any harm!

---

### Inspiration took from [LostSec](https://www.youtube.com/@lostsecc)

---
