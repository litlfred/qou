---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-031-55-patience-sorting
section_title: "Patience Sorting"
section_number: 5.5
pages: 112-115
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.994
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
The presentation of patience sorting that we describe here follows the algorithm as given by Aldous and Diaconis in [@AldousDiaconis]. Patience sorting is a type of one person card game. Imagine that we have a deck of cards with the numbers $1,\dots,n$ on them. We shuffle the deck thoroughly, and put the cards in a pile face down. We turn the cards face up one at a time and put them into a pile according to the following rule:\
*A low card may be placed on top of a higher card (i.e. a 2 on top of a 7), but a higher card must be placed into a new pile to the right of the current piles*.\
The object of the \"game\" is to finish with the fewest piles.

As a short example, let suppose that we have a pile of cards labeled $1,\dots,6$. Let us shuffle them (uniformly at random) and suppose that we end up with the permutation $$4\;\;\;1\;\;\;3\;\;\;2\;\;\;6\;\;\;5$$ with the $4$ on the top of the deck, and the $5$ on the bottom. To begin the patience sorting algorithm, we start with the card $4$, which will be the beginning of our first pile. The next card that we draw is a $1$. Since this is less than $4$, it can go on top of the four in the first pile, so that our piles look like $$\begin{array}{c}
1 \\
4
\end{array}$$ Next we draw a $3$. Since this is larger than $1$, it cannot go to the top of the pile, it must start a new pile. Now we have $$\begin{array}{ccc}
1 & 3 \\
4 &
\end{array}$$ We next add the $2$ to the top of the second pile, since $2>3$. $$\begin{array}{ccc}
1 & 2 \\
4 & 3
\end{array}$$ Adding in $6$ requires us to make a new pile $$\begin{array}{ccc}
1 & 2 & 6 \\
4 & 3 & 
\end{array}$$ We can then place the last card, $5$, on top of the third pile giving us $$\begin{array}{ccc}
1 & 2 & 5 \\
4 & 3 & 6
\end{array}$$ Notice that we end up with $3$ piles. Notice also that the length of the longest increasing subsequence of the permutation is $3$. Once such subsequence is $$1 \; \; \; 3 \; \; \; 6$$ and there are several more, but none of length more than $3$. It turns out that this is not a coincidence. The following theorem is due to Aldous and Diaconis [@AldousDiaconis]

::: thm
With a given deck $\pi$, patience sorting played with the greedy strategy ends with exactly $\ell(\pi)$ piles. In addition, the game played with any legal strategy ends with at least $\ell(\pi)$ piles.
:::

::: proof
*Proof.* Suppose that we have cards $a_1 < a_2<\dots <a_k$ an increasing subsequence in our pile. Then under any legal strategy, each $a_i$ must be placed in a stack to the right of $a_{i-1}$, since any card placed on top of $a_{i-1}$ must be less than the value on $a_{i-1}$. This implies that the final number of piles must be at least $k$, and since this is the length of an arbitrary increasing subsequence, the number of piles must be at least $\ell(\pi)$. Furthermore, suppose we choose the greedy strategy, where we *only* start a new pile if we are forced to. Suppose each time we put a card $a$ into any pile other than the first pile, we place a pointer from that card to the card on the top of the pile immediately to the left. Notice that this card will always be less than our current card. At the end of the game, if we follow the pointers backward from the top card on the last pile, we will have an increasing subsequence whose length is the number of piles. ◻
:::

Using this theorem and the patience sorting algorithm, it is possible to have a computer compute the longest increasing subsequence of a Mallows permutation. The Python code for such a program is included in the appendix. The following figures show a histogram for the length of the longest increasing subsequence of a permutation of length $n=10,000$, run $200$ times under the uniform distrubution and the Mallows distribution for varying values of $q$.

![Length of the longest increasing subsequence of a uniform permutation of length $10,000$](Mallows_sim.png){width="4in"}

![Length of the longest increasing subsequence of a Mallows permutation of length $10,000$ with $q=0.99$](Mallows_99.png){width="4in"}

![Length of the longest increasing subsequence of a Mallows permutation of length $10,000$ with $q=0.88$](Mallows_80.png){width="4in"}

Unfortunately, we were unable to get too much useful information out of our simulations due to the fact that we did not have enough computing power to run the algorithm for big enough permutations. We computed statistics (mean, variance, skewness, kurtosis) for our permutations in hopes of matching the experimental data to what was expected for a type of Tracy Widom distribution, but the results were inconclusive.
