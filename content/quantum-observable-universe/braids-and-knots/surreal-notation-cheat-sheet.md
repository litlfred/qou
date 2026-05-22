**Cheat sheet for first-time readers of surreal notation.**
The full surreal-number formalism — Conway construction, birthday
function, sign sequences, standard-part functor, Hahn series — is
developed in the **surreal-numbers appendix**
([`app:surreals`](#app:surreals)). What follows is a one-page
reading aid sufficient to follow the substrate-level uses of
$\omega$ and $\varepsilon$ in this chapter and in
[the Millennium-bound discussions](#sec:millennium-bounds-via-surreals)
of the appendix.

| Symbol | Reading |
|--------|---------|
| $\mathbf{No}$ | The class of surreal numbers (Conway 1976). Contains $\mathbb{R}$ as a proper subclass plus infinite and infinitesimal elements. |
| $\omega$ | The surreal representation of the first infinite ordinal. $\omega > n$ for every $n \in \mathbb{N}$ (but $\omega - 1$, $\omega/2$, $\sqrt{\omega}$, $\ldots$ are also infinite surreals — there is no smallest infinite surreal). Concretely, $\omega = \{\,0, 1, 2, \dots \,\mid\,\,\}$ in Conway's $\{L \mid R\}$ form. |
| $\varepsilon$ | The positive infinitesimal defined as $1/\omega$. $0 < \varepsilon < 1/n$ for every $n \in \mathbb{N}$ (but $\varepsilon/2$, $\varepsilon^2$, $\ldots$ are also infinitesimal — there is no smallest positive infinitesimal). The substrate parameter $q$ in this paper is built from $\varepsilon$ via [the $q$-from-$\varepsilon$ relation](#def:q-from-epsilon). |
| $1 + \varepsilon$ | An **infinitesimal lift** of $1$. The "relax strict equalities to $1 + \varepsilon$" pattern in the appendix [(`sec:relaxing-strict-equalities`)](#sec:relaxing-strict-equalities) replaces every $x = 1$ with $x = 1 + \varepsilon$ for some surreal infinitesimal $\varepsilon$. |
| $\mathrm{st}\!:\,\mathbf{No}_{\text{fin}} \to \mathbb{R}$ | The **standard-part functor** on finite (non-infinite) surreals — sends $1 + \varepsilon$ to $1$, sends $\omega^{-1}$ to $0$, sends every finite real to itself. Replaces the classical limit; see [`sec:standard-part-classical-limits`](#sec:standard-part-classical-limits). |
| $\mathrm{ord}_\omega\,x$ | The **$\omega$-adic order** — leading exponent of $x$ in Conway normal form. Direct surreal analogue of $\mathrm{ord}_p$ in $p$-adic analysis. Used to grade $\mathcal{H}_q$ and to formulate Goncharov-period-depth identifications. |
| $\{L \mid R\}$ | Conway's **simplest-form construction**: a surreal whose left set is $L$ and right set is $R$. Birthday-graded; the surreal's complexity is the minimum number of construction steps from $\{\,\mid\,\} = 0$. |
| $b(x)$ | **Birthday** of a surreal $x$ — the ordinal at which $x$ first appears in the Conway construction. $b(0) = 0$, $b(1) = b(-1) = 1$, $b(\omega) = \omega$, $b(\varepsilon) = \omega$. |
| $a \sim b$ | $a$ and $b$ have the **same standard part** — i.e. $a - b$ is infinitesimal (or zero). Used in Millennium-bound statements: the surreal bound holds **up to a $1 + \varepsilon$ multiplier**, which collapses to equality under $\mathrm{st}$. |
| $a \prec b$ | $a$ is **infinitesimal relative to** $b$, i.e. $|a/b|$ is infinitesimal. Conway's asymptotic-domination order. |

**When you see $\varepsilon$ in the substrate-level definitions
below** — primarily in
[`def:reeb-epsilon`](#def:reeb-epsilon),
[`def:q-from-epsilon`](#def:q-from-epsilon),
and the joint Galois-braid action — read it as "the positive
infinitesimal $1/\omega$". You do not need the appendix machinery
to follow these definitions.

**When you see a surreal-bound statement** — e.g.
[BSD](#rem:bsd-surreal-bound),
[Collatz](#rem:collatz-surreal-bound), or the unified
[graded-Mikusiński bound](#rem:surreal-bounds-graded-mikusinski) —
the cheat-sheet entry for $\mathrm{st}$ and $a \sim b$ is
the only piece you need; the bound says "the inequality holds up
to a $1 + \varepsilon$ factor", and applying $\mathrm{st}$
recovers the classical statement.

For the full Conway construction, sign sequences as birthday-graded
braid words, the Bloch-Suslin / Borel discharge of the keystone,
and the standard-part functor's behaviour on archimedean limits,
read the appendix in order. For the substrate-level applications in
this chapter, this cheat sheet is sufficient.
