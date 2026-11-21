---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-017-45-discussion
section_title: "Discussion"
section_number: 4.5
pages: 28-29
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.994
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:A Pattern}

Of the four classes of black holes we have looked at, three worked perfectly. Neutral black holes (of any size and in any dimension), spinning BTZ black holes, and small charged black holes all had action growths that, when fed into our complexity equals action formula, gave rates of change of complexity that exactly saturate our bound.

Large charged black holes did not work. We found that a naive calculation of their rate of growth of action implied a complexification rate that was too large. While the rate satisfied the $2M$ bound of Eq.~\ref{C-bound}, it violated the tighter $2(M - \mu Q) - 2(M - \mu Q)_\textrm{gs}$ bound of Eq.~\ref{CQ-bound} that we conjectured should be satisfied by systems with conserved charge.

We believe we understand why the naive calculation of large charged black holes doesn't work, and why the other calculations do work. We suspect that it is to do with hair.

In theories with light charged particles, a ball of charge may form around a charged black hole. The hair becomes progressively more important as extremality is approached. At fixed $\mu$, this hair affects both the charged black hole and the ground state, and renders unreliable the calculation of the action, the calculation of $M - \mu Q$, and indeed the whole classical geometry. At fixed chemical potential $\mu > m/q$, the minimum of $M - \mu Q$ will feature a ball of charged particles (for $\mu > G^{-1/2}$ this ball will lie outside a black hole; for $G^{-1/2}>\mu >m/q$ there will be only a ball and no black hole).


Indeed, it should have been obvious that light charged particles will disrupt our analysis. Consider the claim that a black hole of mass $M$ and charge $Q$ is the fastest computer with that value of mass and charge.  In general this is obviously false.  Consider the case of an extremal black hole, which does not complexify at all; its complexification rate is zero. Let's compare that with a system consisting of a neutral black hole and a collection of electrons at a safe distance.  If we assume that the mass  and charge of the electron satisfy
\be
m< \frac{q}{\sqrt{G}}
\ee
then removing charge $Q$ in the form of electrons leaves the remaining neutral black hole with positive mass. This then does complexify, and therefore  charged black holes cannot generally be the fastest computers of a given mass and charge.

This explains why  our naive calculation of large charged black holes did not work. Now let's explain why small charged black holes  do work.  The reason is supersymmetry. In a sufficiently supersymmetric theory the BPS bound guarantees that there will be no light charged particles: every particle has $m \geq q /\sqrt{G}$. This means that sufficiently supersymmetric black holes are not susceptible to the formation of hair. Whenever our theory is a consistent truncation of a sufficiently supersymmetric theory, our calculations must be reliable.
Because flat space Reissner-Nordstrom emerges as the limit of the Strominger-Vafa \cite{StromingerVafa96}  $D1-D5$ system when the three charges are all equal \cite{CallanMaldacena96}, small Reissner-Nordstrom black holes had to work.

Similarly, rotating BTZ black holes had to work. A particle cannot have large angular momentum without having large energy; in addition, extremal BTZ black holes are known to have supersymmetric UV completions \cite{Coussaert:1993jp}.


On the other hand, large RN black holes in AdS did not have to work. We know of no examples in which they are sufficiently supersymmetric that our calculations had to be reliable. We had no reason to trust our naive calculations; and our naive calculations give us no reason to distrust our conjectures.
