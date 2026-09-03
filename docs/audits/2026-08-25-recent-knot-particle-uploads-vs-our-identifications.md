# The recent knot-particle uploads: same ontology, opposite stance on identification — and one energy law

**Date:** 2026-08-25
**Question asked:** do any of the knot-particle papers committed in the last hour
make the same identifications (e.g. electron) as we do, and do they point to a
missing term for binding?
**Status:** read. Answers below are from the ingested text, quoted.

## Answer in one line each

| paper | same identifications? | points to a binding term? |
|---|---|---|
| `symmetry-11-01298` — Asselmeyer-Maluga, *Braids, 3-manifolds, elementary particles* | **same ontology, and it explicitly rejects the identification programme** | **no** — no nuclear content at all |
| `arxiv-2106.01332v4` — Gresnigt–Marcianò–Zappala, *Braided matter interactions ... via 1-handle attachment* | Bilson–Thompson braids of **three** ribbons; no per-particle knot table in the text | **no** — supplies interaction *dynamics*, but no energy functional |
| `arxiv-hep-th-9610193v1` — Faddeev–Niemi, *Knots and Particles* | not an identification paper | **the only one with an energy law** — see §3 |

## 1. Asselmeyer-Maluga contradicts the corpus's canonical-knot-ID programme

Same ontology as ours: fermions are hyperbolic **knot complements**, bosons are
the torus bundles between them, and *"bosons and fermions are represented as
3-braids"* — the same 3-strand count the corpus uses in $H_{3A}(q)$. (His 3 comes
from a 3-fold branched covering $T^2 \to S^2$ with six branch points, a 6-plat
read as a 3-braid; the corpus's 3-per-nucleon is colour. Whether these are the
same 3 is **not** established by the coincidence, and this note does not claim it.)

On identification he is explicit, and it is the opposite of our position:

> *"which knot is related to a fermion like the electron? **However, this question
> is meaningless in our approach.** The knot/link complements are induced from the
> singularities of the branching set ... the branching set, a knot or link, of a
> 3-manifold is **not unique**."*

and

> *"Our model agrees with the Bilson–Thompson model but with the exception that we
> do not fix the braid. In particular, **we do not believe that the difference
> between an electron and myon is given by a different braid.**"*

**That is a direct challenge to a load-bearing corpus claim.** CAL-2's numerical
proxy is `m_μ/m_e = Vol(4₁)/ℏ_q²` — the muon/electron ratio *is* a knot
distinction here (the figure-eight), which is exactly what he denies. It also
bears on `conj:canonical-knot-id-sdp`, whose production source already admits
*"that IS a form of AME-driven fitting"*
([`2026-08-25-knot-id-is-an-admitted-fit.md`](2026-08-25-knot-id-is-an-admitted-fit.md)).

His stated ground is **non-uniqueness of the branching set** — many knots present
the same 3-manifold. That is a real objection with a specific shape, and the
corpus's answer to it, if there is one, would be that the Markov trace is an
invariant of the *closure*, not of the presenting braid. Whether that answers his
objection or merely restates the difficulty is not settled here.

**This is a useful adversarial datapoint, not a refutation.** It is a different
framework's methodological choice, not a proof that ours is wrong. Recorded so
the corpus's identification programme is at least aware it is contested in the
literature it shares an ontology with.

## 2. Neither braid paper has nuclear binding

`symmetry-11-01298`: zero occurrences of "binding", "nucleon", "nucleus" or
"MeV" across all 22 sections; two "mass" hits, both about the Higgs and neutrino
masses. It reaches charge (as a Dehn twist of the boundary torus) and generation
count, not nuclear energetics.

`arxiv-2106.01332v4` is about *interactions* — 1-handle attachment as a
non-local, graph-changing move that lets braided excitations interact at all,
which the model previously lacked. Structurally that is the right neighbourhood
for "how do two nucleons combine", but the paper supplies **no energy**: the
result is that interaction is *possible*, not what it costs.

## 3. Faddeev–Niemi carry an energy law, and it is not per-block

This is the one with quantitative content. Verbatim from the ingested text:

> *"the existence of nontrivial knotted vortex solutions in (2) is strongly
> suggested by the lower bound $H \geq c \cdot |Q_H|^{3/4}$ [14]."*

with $Q_H$ the **Hopf invariant** and [14] Vakulenko–Kapitanski (1979). The
Hamiltonian is $H = E_2 + E_4 = \int d^3x\; \tfrac{g}{2}(\partial_\mu \vec n)^2 +
e^2 F^2$ — the Faddeev model, related to the SU(2) Skyrme model restricted to
$S^2 \subset SU(2)$ *"but its topological features are different"*.

**Why this is worth noting for the binding gap.** The corpus's failure at ⁴He is
that the per-block / pairwise form saturates: `B_sym/A` tops out at 2.998
MeV/nucleon against nature's 8.790, and ⁴He exceeds the complete-graph pairwise
ceiling by 11.12 MeV
([`2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md)).
A bound of the form $|Q_H|^{3/4}$ is **neither per-block nor pairwise** — it is a
single non-linear functional of a global topological charge. That is the *class*
the missing term has to live in.

**And it is not a drop-in — the direction is wrong as stated.** $Q^{3/4}$ is
*sub*-linear, so if $Q_H$ scaled with $A$ the binding per nucleon would *fall*
like $A^{-1/4}$, whereas the corpus needs it to *rise*. It sits between the
SEMF's surface term ($A^{2/3}$) and its volume term ($A^1$), which is
suggestive — and suggestive is all it is. **Do not read a fit into that**: no
relation between $Q_H$ and the corpus's $A$, or between the Faddeev Hamiltonian
and the Markov trace, is established anywhere. The corpus's own
`hopf-link-non-magic` has `Vol(Hopf) = 0`, so the Hopf object is already
*degenerate* in our setting, which cuts against a naive transfer.

**What it actually supplies:** a precedent, from a paper now in the library, that
a knot-energy functional need not be additive over blocks at all — and a named,
citable lower bound to compare a candidate closure against.

## 4. What this note does not claim

That Asselmeyer-Maluga refutes the corpus's knot identifications; that the
corpus's 3-braid and his 3-braid are the same 3; that $|Q_H|^{3/4}$ is, or
approximates, the missing binding term; or that the Faddeev Hamiltonian relates
to the Markov trace. Each of those would need to be shown, and none is shown
here.
