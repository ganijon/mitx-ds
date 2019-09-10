# Case Study_1.2 

## Finding_Themes


Finding the topics or themes in a collection of text.

Clustering by itself can be a little problematic, because a single document might exhibit multiple topics.

It makes a lot of sense to use a model that lets each data point, each article, exhibit multiple topics.

Recall that one term for this is a Mixed Membership Model. A particularly popular model in this vein is known as Latent Dirichlet Allocation or LDA.

To see what it looks like to use this model in practice, let's use LDA to analyze what MIT faculty are working on in their research.

To find hidden groups of research topics among the faculty, where a faculty member can work on multiple research topics at a time, we're going to use a mixed membership model like LDA.

To create our data set, we assemble abstracts from each professor's published papers for a total of over 900 abstracts. Each abstract is a text document that briefly describes a particular piece of research
a professor conducted.

A common pre-processing step for LDA is to remove the most common words, words like of, the, and a, that don't tell us much about a document, and the least common words, words so rare that they don't tell us much across documents. 

Just like we need to specify the number of clusters in advance in k means, we need to specify the number of topics in advance for LDA. And just like we called the number of clusters k for clustering, here we can call the number of topics k.

We used heuristics to choose the number of clusters in a clustering problem.
Similarly, we can use heuristics to choose the number of topics and topic modeling.

Heuristics for this problem suggest that smaller k yield more meaningful results. So, we choose k equals 5 topics.

At this point, we can run a Stochastic Variational Inference algorithm for LDA and look at the results.

Just as in clustering we discover clusters, in topic modeling, we discover topics.

So the first thing to do is to look at the topics. We can visualize topics by looking at the most
common words in each topic. 

In this case, one of the topics has words like quantum, state, system, channel, and information. This topic seems to be capturing a line of research on quantum computation communication and information
theory.

Another topic has words like algorithm, model, problem, and time. This is a topic on traditional computer science themes, like algorithms, and complexity theory.

N is a symbol typically used to express the number of data points in a data problem.

Yet another topic has words like temperature, graphene, phase, and gate.

These are words related to material science. So one of the first things we notice here
is that research in the department is pretty diverse, which makes sense since the department contains both electrical engineering and computer science.

We can also look at the topics of research in each lab. To generate this figure, we consider all the researchabstracts within each lab, and show what proportion of the research text
falls into each topic category. 

First, we notice that CSAIL and LIDS are both dominated by the algorithms topic.
This makes sense. CSAIL essentially contains all of the computer science professors within the EECS department.

And the faculty in LIDS work on similar problems, with perhaps a bit more focus on information theory.
We see this reflected in the higher proportion of the topic on quantum and information-related themes.
RLE and MTL both contain words related to circuits. So again, this makes sense since these labs
form the more traditional lab-based side of electrical engineering.

Finally, MTL is distinguished by a significant proportion of research text related to material science.

So the nice thing about this analysis is that we learned all of these topics and the breakdown of labs by topic automatically.

Few people, including professors at MIT, would be able to describe exactly what all these different MIT professors work on.

But we were able to automatically pick up what words go together and describe coherent themes
of this research.

And we were able to distinguish different parts of the department by the different types of research
that goes on there. You could imagine doing a similar analysis for a company,
or for the user base of an app.

What are the different themes users talk about in their post on a forum?
And how different forms differ in what they focus on?

This type of analysis can be very useful for understanding a user base, or for generating a quick summary of a lot of text documents that might otherwise be difficult to navigate.

In this video, we've seen how extensions of clustering can be useful in practice.

In particular, we investigated a data analysis problem with human-generated tax using Latent Dirichlet Allocation, or LDA.
