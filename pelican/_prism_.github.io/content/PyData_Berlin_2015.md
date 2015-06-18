Title: PyData Berlin 2015
Date: 2015-06-18 00:00:00
Modified: 2015-06-19 00:00:00
Category: python
Tags: python, data, berlin, pydata
Slug: PyDataBerlin2015
Authors: prismv
Summary: PyData Berlin 2015

After a visit of [PyData Berlin 2015](http://pydata.org/berlin2015)
event, which took place 29.-30. May at location
[Betahaus](http://www.betahaus.com), I wrote down some links as a
reminder, and decided then to put them here alongside with some
thoughts on given topics.

Actually there were talks as given on meeting site - 'related to the
use of Python in data management and analysis' - from variety of
fields, but with emphasis on application of machine learning.

In 2014 PyData Berlin event was a [talk of Travis
Oliphant](https://www.youtube.com/watch?v=d9Qm3PPoYNQ) , during which
also 'PyData: the First 20 Years' were summarized on a slide. Actually
this story began with basic matrix calculation packages that were
precursor of current standard [NumPy](http://www.numpy.org) and
extensions like [SciPy](https://www.scipy.org) and
[matplotlib](http://matplotlib.org). With
[pandas](http://pandas.pydata.org) and several machine learning
packages, e.g. [scikit-learn](http://scikit-learn.org), the PyData
ecosystem rivals [R](http://www.r-project.org) and interacts with
'big' Java-driven 'big data' solutions centered on
[apache.org](https://projects.apache.org/indexes/category.html#big-data) -
as described
e.g. [here](http://www.blue-yonder.com/blog-e/2014/11/12/environment-choose-data-science).

Topics presented and discussed in Berlin this year were commented in
'official'
[#PyDataBerlin](https://twitter.com/hashtag/PyDataBerlin?src=hash)
twitter feeds, and [videos](https://www.youtube.com/user/PyDataTV) are
on-line.

The keynote from [Matthew
Rocklin](http://matthewrocklin.com) from [Continuum
Analytics](http://continuum.io) was about
[Dask](http://dask.pydata.org/), which seems to be a quite elegant
approach to get 'instantly' multi-core performance for a large subset
of NumPy functionality by parallel processing. This topic leads
usually to hints about limitations for multi-threaded data management
because of [GIL](https://wiki.python.org/moin/GlobalInterpreterLock),
and consequently one of Matthew's message was to get rid of this in
main parts of PyData module ecosystem ([with
nogil](http://docs.cython.org/src/userguide/external_C_code.html#nogil)
statement in cython).

[Valentin Haenel](http://haenel.co) talked about Blosc and related
higher-level packages (see links on his homepage). Especially the
'columnar data container' [bcolz](https://github.com/Blosc/bcolz) could
be considered as an light-weight alternative for HDF5 file format (actually
[PyTables](http://www.pytables.org) offers also Blosc-based
compression filter).

[Claas Abert](https://github.com/c-abird)'s talk about numerical
treatment of PDE with Numpy gave impresison about one 'classic' use
case for PyData packages, i.e. physical simulations by
finite-difference and finite-elements methods of [micromagnetic
problems](http://micromagnetics.org). The finite-elements package is
based on [FEnICS](http://fenicsproject.org/). Number crunching
involves also optimization of Python code, and an overview on
possibilities was given. Thanks for getting a hint about new JIT
compiler: [HOPE](https://github.com/cosmo-ethz/hope)!

Mobile app marketing was one example of 'new' 'Big Data' and their
challenges. Nakul Selvaraj from [Trademob](http://www.trademob.com)
explained demands for real-time monitoring, and his colleague Tobias
Kuhn gave some insights about statistical methods with specific
algorithms like [t-digest](https://github.com/trademob/t-digest) used
e.g.  for tracking of anomalies, or how to decompose trends on top of
seasonal variations.

There were 2 talks from [Pivotal](https://pivotal.io) folks. [Cloud
Foundry](http://cloudfoundry.org) was mentioned as their
[PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) product,
and it's interesting to see what open source is [used
@Pivotal](https://pivotal.io/open-source). Here smart GPS tracking of
cars was given as one example of
[IoT](https://en.wikipedia.org/wiki/Internet_of_Things). In this study
presented by Ronert Obst [Random
Forests](http://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm)
were used to learn and classify possible driven routes. Although
[Spark](https://github.com/apache/spark) usage was mentioned here and
in other talks, it was also hinted to
[Flink](https://github.com/apache/flink) as alternative with different
memory model and ability to process data
[streams](http://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/languagebinding/api/java/python/streaming/PythonStreamer.html).

On Friday the presentation session ended with 'Get Together', but one
should not forget to mention the (en)lightning talks just before. I
pick two: Matthew Rocklin gave short example to show what the benefit
of [pandas' dtype
category](http://pandas.pydata.org/pandas-docs/dev/categorical.html#categorical)
is. And the presentation from [Tadej Štajner](http://tdj.si) about
[automatic machine learning](http://tdj.si/automl_pydataberlin.pdf)
with some [code](https://github.com/tadejs/autokit).  So how different
will be future PyData events, if one takes one statement on
[AutoML](http://automl.org) site too serious: 'taking the human expert
out of the loop'?

It was not only a presentation about how [ascribe](https://www.ascribe.io)
uses Python modules, like
[transactions](https://github.com/ascribe/transactions) as 'Bitcoin
for Humans', but in his keynote Trent McConaghy also gave an
interesting view on how blockchains and a suitable protocol
([Spool](https://github.com/ascribe/spool)) under the hood can help
e.g. artists to keep in control of intellectual property of digital
objects.

The keynote of Felix Wick from [Blue
Yonder](http://www.blue-yonder.com) contained really lots of
information not only about technical stuff a data scientist might or
should know, when doing e.g [predictive
analytics](http://www.gartner.com/it-glossary/predictive-analytics). So
in his/her life it might be not bad to know a bit about hype cycles -
but do not care too much. And you should really have a look to the
[video](https://www.youtube.com/watch?v=Fo0Ne2pYWW4), because it
appears to be almost a lecture, which gives a nice introduction on
'data science' in our Big Data world (be it a peak or not ...).

Peadar Coyle very nicely presented an interesting example how [sports
analytics](http://nbviewer.ipython.org/format/slides/github/springcoil/Probabilistic_Programming_and_Rugby/blob/master/Bayesian_Rugby.ipynb#/) -
in this case [6 Nations](http://www.rbs6nations.com) playing Rugby -
can be done by applying bayesian statistical models with
[PyMC](https://github.com/pymc-devs/pymc). Someone in the audience
mentioned that it could be already worth switching to the successor
[PyMC 3](https://github.com/pymc-devs/pymc3) to perform Markow chain
Monte Carlo fitting. Actually
[this](http://nbviewer.ipython.org/github/aloctavodia/Doing_bayesian_data_analysis/blob/master/IPython/Kruschkes_Doing_Bayesian_Data_Analysis_in_PyMC3.ipynb)
notebook seems to be a good tutorial for learning or migration
purposes.

The second presentation of Blue Yonder folks was an
introduction to
[PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
DataFrame objects, which are created to make use of - for instance -
columnar data stored on [Hadoop](http://hadoop.apache.org/) HDFS
clusters in [Parquet](http://parquet.apache.org) format. It was
concluded that such an API for distributed file access is too costly
in terms of efficiency compared to NumPy arrays or Pandas dataframes,
when data fits on one machine.

[Alejandro C. Bahnsen](http://albahnsen.com) presented his work
[CostCla](https://github.com/albahnsen/CostSensitiveClassification),
which examplifies usage of scikit-learn classifications on financial
topics like [credit
scoring](http://nbviewer.ipython.org/github/albahnsen/CostSensitiveClassification/blob/master/doc/tutorials/tutorial_edcs_credit_scoring.ipynb).

Brian Carter (IBM Software Group) gave an overview on web text mining
processes. In this field the [NLTK](http://www.nltk.org) module seems
to be the standard for language processing with Python.

When dealing with similarity of words like Miguel Fernando Cabrera (TrustYou) did with hotel reviews, [word2vec](https://github.com/danielfrg/word2vec) has the metrices needed.




I didn't attend the tutorial sessions, so it will help to have a look
at respective videos, if one wants to learn and understand better
e.g. how interactive graphics e.g. within [IPython
notebooks](http://ipython.org/notebook.html) can be created with
[Bokeh](http://bokeh.pydata.org), how
[Docker](https://docs.docker.com) could be seen in between tools like
virtualenv and 'normal' virtual machines, and what one could use
instead of
[%timeit](https://ipython.org/ipython-doc/dev/interactive/magics.html?highlight=timeit#magic-timeit)
for code profiling.

Someone referred to the
[velox](https://amplab.cs.berkeley.edu/projects/velox) model server,
and I noted also [Luigi](https://github.com/spotify/luigi) for
pipeline creation of batch jobs \- if you remember the right context,
talk or discussion, those were given then feel free to message me
[@RaPrism](https://twitter.com/RaPrism).


<!-- Local Variables: -->
<!-- mode: rst -->
<!-- End: -->
