# overview

create a simple web crawler to scrape HTML pages of the textbook; extract information (title, text); perform basic text processing to display corpus and vocabulary statistics.

# scraper workflow

1. seed url is `https://nlp.stanford.edu/IR-book/information-retrieval-book.html`
2. there are 21 sections and their subsections in the book. each page as a title and a body. extract the title from `<h1>` tags and the body from `<p>` tags.
3. use beautifulsoup to parse the html
4. extract URLs with `find_all()` to find all `<a>` tags and get the `href` attribute
5. if URL is relative, convert it to absolute URL using `urljoin()` from `urllib.parse`.
6. newly discovered URLs should be added to a set to avoid duplicates.
7. 



# notes

Outbound links from seed URL:
- http://cislmu.org
- http://nlp.stanford.edu/%7Emanning/
- http://nlp.stanford.edu/IR-book/essir2011
- http://nlp.stanford.edu/IR-book/html/errata.html
- http://nlp.stanford.edu/IR-book/html/flat.html
- http://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/computing-scores-in-a-complete-search-system-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/dictionaries-and-tolerant-retrieval-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/flat-clustering-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/hierarchical-clustering-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/index-compression-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/index-construction-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/irbook.html
- http://nlp.stanford.edu/IR-book/html/htmledition/language-models-for-information-retrieval-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/link-analysis-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/matrix-decompositions-and-latent-semantic-indexing-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/probabilistic-information-retrieval-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/relevance-feedback-and-query-expansion-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/scoring-term-weighting-and-the-vector-space-model-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/support-vector-machines-and-machine-learning-on-documents-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/text-classification-and-naive-bayes-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/the-term-vocabulary-and-postings-lists-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/vector-space-classification-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/web-crawling-and-indexes-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/web-search-basics-1.html
- http://nlp.stanford.edu/IR-book/html/htmledition/xml-retrieval-1.html
- http://nlp.stanford.edu/IR-book/pdf/00front.pdf
- http://nlp.stanford.edu/IR-book/pdf/01bool.pdf
- http://nlp.stanford.edu/IR-book/pdf/02voc.pdf
- http://nlp.stanford.edu/IR-book/pdf/03dict.pdf
- http://nlp.stanford.edu/IR-book/pdf/04const.pdf
- http://nlp.stanford.edu/IR-book/pdf/05comp.pdf
- http://nlp.stanford.edu/IR-book/pdf/06vect.pdf
- http://nlp.stanford.edu/IR-book/pdf/07system.pdf
- http://nlp.stanford.edu/IR-book/pdf/08eval.pdf
- http://nlp.stanford.edu/IR-book/pdf/09expand.pdf
- http://nlp.stanford.edu/IR-book/pdf/10xml.pdf
- http://nlp.stanford.edu/IR-book/pdf/11prob.pdf
- http://nlp.stanford.edu/IR-book/pdf/12lmodel.pdf
- http://nlp.stanford.edu/IR-book/pdf/13bayes.pdf
- http://nlp.stanford.edu/IR-book/pdf/14vcat.pdf
- http://nlp.stanford.edu/IR-book/pdf/15svm.pdf
- http://nlp.stanford.edu/IR-book/pdf/16flat.pdf
- http://nlp.stanford.edu/IR-book/pdf/17hier.pdf
- http://nlp.stanford.edu/IR-book/pdf/18lsi.pdf
- http://nlp.stanford.edu/IR-book/pdf/19web.pdf
- http://nlp.stanford.edu/IR-book/pdf/20crawl.pdf
- http://nlp.stanford.edu/IR-book/pdf/21link.pdf
- http://nlp.stanford.edu/IR-book/pdf/99back.pdf
- http://nlp.stanford.edu/IR-book/pdf/ir.bib
- http://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf
- http://nlp.stanford.edu/IR-book/pdf/irbookprint.pdf
- http://search.yahoo.com/search?p=0521865719
- http://www.cambridge.org/us/catalogue/catalogue.asp?isbn=9780521865715
- http://www.cis.uni-muenchen.de/personen/professoren/schuetze/
- http://www.stanford.edu/class/cs276/
- https://nlp.stanford.edu/IR-book/information-retrieval-book.html#anchor01
- https://nlp.stanford.edu/IR-book/information-retrieval.html
- https://research.google/people/prabhakarraghavan/