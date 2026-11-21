**Conjecture (conditional).**
Under the [Kashaev volume conjecture](#conj:kashaev-volume-conjecture)
applied to an atomic Hecke element $T_w$ with `Markov closure` knot/link
$K_w$, the multiplicative density prefactor
$\rho_F \in \mathbb{Z}_{>0}$ in the binding-energy formula

$$
  B_{\mathrm{pred}}(K_w)
  \;=\;
  \rho_F \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(K_w)
$$

equals the **joint-tower SDP Wedderburn multiplicity** $\nu_{\mathrm{SDP}}(K_w)$
of the canonical Hecke element $T_w$'s saturating SDP solution in the
$H_{n}(q)$ Wedderburn decomposition:

$$
  \rho_F  \;=\;  \nu_{\mathrm{SDP}}(K_w)
$$

per [`atom-knot-mass-derivation`](#conj:atom-knot-mass-derivation)
§Algorithm step 3 (the joint-tower SDP solve that produces
$\nu_{\mathrm{SDP}}$ as a non-negative integer multiplicity).

## Evidence (two confirmed atoms)

The identity is exact on the SDP-confirmed
hyperbolic atoms (per
[`atom-knot-mass-derivation`](#conj:atom-knot-mass-derivation) line 265):

| Atom | $K_w$ | $\rho_F$ (legacy) | $\nu_{\mathrm{SDP}}$ |
|------|-------|-------------------|----------------------|
| ${}^{3}\mathrm{H}$ (T)  | knot $8_{11}$     | 2 | 2 |
| ${}^{3}\mathrm{He}$     | link $L_{6a4}$    | 2 | 2 |

The deuterium row that once headed this table has been removed, and the
removal is not bookkeeping. It read
${}^{2}\mathrm{H} \mid 6_2 \mid 1 \mid 1$, assigning the deuteron the census
knot $6_2$ with $\mathrm{Vol} \approx 4.40$. The canonical deuteron knot is the
braid closure (trefoil / Hopf), with $\mathrm{Vol} = 0$; the $6_2$ assignment is
retired, and the deuteron binding is not a hyperbolic-volume term. Since the
identity's own formula is
$B_{\mathrm{pred}}(K) = \rho_F \, \mathfrak{m}_e \, \mathrm{Vol}_{\mathrm{hyp}}(K)$,
at $\mathrm{Vol} = 0$ it returns $B_{\mathrm{pred}} = 0$ for **every** value of
$\rho_F$ — so that row could not constrain the prefactor even in principle. It
was not a stale entry contributing weak support; it was contributing none.

The evidence base for the $\nu_{\mathrm{SDP}}$ pattern is therefore **two
points**, both equal to $2$, not three points reading $1, 2, 2$. The $1$ was the
row now removed, so the *variation* in that pattern came entirely from it.

Read this together with an operational finding:
six operational definitions of $\nu_{\mathrm{SDP}}$ were computed and **none**
reproduces the legacy triple, and the committed values carry the methodology tag
`"manual-historical-volume-match"` — they are hand-assigned rather than derived.

The ${}^{4}\mathrm{He}$ case uses the magic $A \cdot 8G$ closure rule rather than a
census knot. A binding-arbiter probe against AME2020
does **not** confirm an
integer $\nu_{\mathrm{SDP}}(⁴\mathrm{He})$: the data-pinned prefactor is
$\rho_F(⁴\mathrm{He}) = B_{\mathrm{AME}}/(m_e A\,8G) \approx 1.889$, which sits
**strictly between** the isospin count ($2T{+}1 = 1$, $T{=}0$) and the monotone
Wedderburn count ($A{-}1 = \mathrm{sc}(3A) = 3$). No clean categorical integer
count reproduces $1.889$; rounding it to $2$ has no derived origin.
Consequently the identity $\rho_F = \nu_{\mathrm{SDP}} \in \mathbb{Z}_{>0}$ is
**scoped to the census-knot / linear-chain atoms**
(${}^{3}\mathrm{H}$, ${}^{3}\mathrm{He}$), where $\rho_F = A{-}1$ is exact and the
SDP framing is canonical. At the doubly-magic point the prefactor is an
**empirical effective binding coefficient** ($\approx 1.89$, Coulomb-corrected
$\approx 1.94$), not an integer categorical multiplicity.

## Categorical home

This identity is of the **MacMahon-style partition-algebra** type.
The Wedderburn multiplicity of $T_w$'s SDP solution is a
partition-algebra count: it is the dimension of the saturating
projection in the irreducible-block decomposition
$H_n(q) \cong \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)$.
The agreement with the Kashaev density factor identifies
$\rho_F$ as such a count.

## Conditional structure

The conjecture is **conditional on the joint-tower SDP completeness**:
i.e. the joint-tower SDP solver of
the canonical formalism, which does not yet exist, gives a unique
non-negative integer
$\nu_{\mathrm{SDP}}(K_w)$ for every bound-state knot $K_w$. Until that solver
is available, the identity is verified on two census atoms and
extrapolated to ${}^{4}\mathrm{He}$ with explicit caveat. The hypothesis
asserts, for each atom $a$ with volume $\mathrm{Vol}(a) > 0$ and with $m_e > 0$,
a positive integer $\nu_{\mathrm{SDP}}(a)$ such that $\rho_F(a) = \nu_{\mathrm{SDP}}(a)$,
together with the binding formula $B_{\mathrm{pred}}(a) = \rho_F(a)\, m_e\, \mathrm{Vol}(a)$.

The quantities $\rho_F$, $\mathrm{Vol}$ and $m_e$ are **given data** rather than
existentials, so the hypothesis is refutable: a prefactor lying strictly
between two consecutive naturals — as the ${}^{4}\mathrm{He}$ datum
$\rho_F \approx 1.889$ does — admits no $\nu_{\mathrm{SDP}}$ at all.

**The hypothesis is not established.** That is the open state: establishing it
would require supplying $\nu_{\mathrm{SDP}}$, and no operational definition in the
corpus yet reproduces the confirmed $1, 2, 2$. The hypothesis deliberately does
*not* identify $\nu_{\mathrm{SDP}}$ with any SDP construction — the Wedderburn
saturating projection whose dimension it is meant to be is not constructed
here — so what it states is the positive-integrality of the prefactor and the
binding formula it feeds, and nothing more.

## Notation hazard resolved

Before the present convention, three distinct quantities used the symbol $\rho$
in QOU compute and content (per
[`atom-knot-mass-derivation`](#conj:atom-knot-mass-derivation) §Notation):

- $\nu_{\mathrm{SDP}}$ — integer Wedderburn multiplicity (this conjecture)
- $\rho_K$ — CODATA-fit density per knot
- $\rho_F$ — Kashaev prefactor in the formal derivation (unnamed, compute-only)

The present convention consolidates around the canonical $\nu_{\mathrm{SDP}}$ name,
removing the third unnamed $\rho$.

## Where $\nu_{\mathrm{SDP}}$ is used

- the atom assignment of the binding computation, which reads
  $\nu_{\mathrm{SDP}}$ and emits $B_{\mathrm{pred}} = \nu_{\mathrm{SDP}} \cdot m_e \cdot \mathrm{Vol}(K)$
- [`atom-knot-mass-derivation`](#conj:atom-knot-mass-derivation)
  §Algorithm step 3 — supplies $\nu_{\mathrm{SDP}}$ via joint-tower SDP

## What remains open

1. **${}^{4}\mathrm{He}$ resolved (negative).** The binding-arbiter probe
   found $\rho_F(⁴\mathrm{He}) \approx 1.889$ — not an integer, and no
   categorical count derives the cap at $2$ (see §Evidence). The open successors
   are sharper: (a) is $\rho_F$ even integer-valued at doubly-magic nuclei? and
   (b) derive the doubly-magic prefactor directly (including Coulomb), rather
   than rounding $1.89 \to 2$. The census-knot atoms
   (${}^{3}\mathrm{H}$, ${}^{3}\mathrm{He}$) remain the exact domain of the
   $\rho_F = \nu_{\mathrm{SDP}}$ identity; ${}^{2}\mathrm{H}$ left that domain
   when its knot assignment was retired (see §Evidence).
2. **Extend joint-tower SDP to ${}^{5}\mathrm{Li}$, ${}^{6}\mathrm{Li}$, ${}^{7}\mathrm{Li}$** — the A$\in${5,6,7} gap
   needs $\nu_{\mathrm{SDP}}$ values; the wider atom$\to$knot census is
   deferred until the full SDP solver is available.
3. **Extend joint-tower SDP to α-cluster atoms (${}^{8}\mathrm{Be}$ and up)** — the
   α-cluster rule inherits $\rho_F = 2$ from ${}^{4}\mathrm{He}$; verifying
   $\nu_{\mathrm{SDP}} = 2$ across the α-cluster recursion would close
   the inheritance step.

## Cross-references

- Underlying Kashaev volume conjecture:
  [`kashaev-volume-conjecture`](kashaev-volume-conjecture.md)
- $\nu_{\mathrm{SDP}}$ algorithmic definition:
  [`atom-knot-mass-derivation`](atom-knot-mass-derivation.md)
  §Algorithm step 3
