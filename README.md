Hearthstone Deck Generator
==========================

Written by aolgin and dyer.w

Objective
---------

The objective of this project is to create an algorithm that will analyze current deck-ranking data and generate a fairly-strong deck for Blizzard's *Hearthstone: Heroes of Warcraft*.

Project Overview
----------------

Hearthstone Deck Generator will scrape several pages of Hearthpwn.com's top decks of the week and, based on card and combination frequency, generate a 30-card deck usable in Hearthstone that *should* at least provide a strong foundation for a deck, if not a good deck overall.

Data Model
----------

After scraping our deck data into a python dictionary, using [NetworkX](https://github.com/networkx/), we convert it into a weighted, undirected graph, where the cards are nodes, the edges are indications that those two cards showed up in the same deck, and the edge weights are the frequencies of such occurrences.

Also, it should be noted that in cases where a deck contains two instances of a card (e.g. two Murlocks), there will be one node for a single Murlock and another distinct node for a set of two Murlocks.

Related Algorithms
------------------

When researching existing algorithms for this project, we came across several variations for Wizards of the Coasts' *Magic: The Gathering* and not much for *Hearthstone*. Neither of them provided exactly what we wanted, but they gave us a good insight into how to approach this.

elvishjerricco created [his own MTG Deck Builder]( https://github.com/ElvishJerricco/MTGBuilder) which could handle combinations of various sizes and decks of various types.

His algorithm is an improvement on [Frank Karsten's Aggregate Deck Builder](http://www.channelfireball.com/articles/magic-math-a-new-way-to-determine-an-aggregate-deck-list-rg-dragons/) for MTG, would could handle building an aggregate deck, but ran into issues with combinations and synergy.

While Hearthstone is a somewhat simpler game in terms of mechanics and card types than MTG, it is still different enough that we needed to come up with our own take on the algorithm.
