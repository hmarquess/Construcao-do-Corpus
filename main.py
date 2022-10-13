nlp=spacy.load("en_core_web_sm")
url = ["https://en.wikipedia.org/wiki/Natural_language_processing", "https://www.gyansetu.in/what-is-natural-language-processing/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8120048/", "https://languagelog.ldc.upenn.edu/nll/?p=2946", "https://www.fcg-net.org/"]

for x in url:
  result = requests.get(x).text
  soup = BeautifulSoup(result, 'lxml')

  text = "".join([i.text for i in soup.find_all('p')])

  doc = nlp(text)

  for sent in doc.sents:
    print(sent)



