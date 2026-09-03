# The spectral-sequence work is a no-go, not a tool — and the extensive term is on a different filtration

**Date:** 2026-08-25
**Question asked:** can the corpus's spectral-sequence work help close the mass /
binding gaps, and does the ingested literature help?
**Status:** corpus-grep + read. Two new findings, one unmined source, one Lean defect.
**Prior work this builds on, not repeats:** bean `wpdb`,
[`2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated`](2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md),
[`2026-08-16-three-gb-filtrations-one-name`](2026-08-16-three-gb-filtrations-one-name.md),
[`2026-08-21-webster-williamson-molien-lead-for-equivariant-index`](2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md).

## Short answer

**No, and the reason is worth more than the answer.** The corpus's spectral
sequence is asserted to **collapse**, so by construction it has no higher-page
differentials to donate. Read at face value it is an *obstruction* — a statement
that nothing beyond the per-partition centre exists inside $H_n(q)$ — which is
the wrong sign for a gap that needs a *new* term.

The term the binding gap actually needs already exists in the corpus, on a
**different** filtration, and the connector between the two is the thing nobody
has established.

## 1. What the corpus's spectral sequence says

[`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md):
for semisimple $A = H_n(R,q)$, Hochschild cohomology vanishes in positive
degrees, so the GB-filtration spectral sequence collapses at $E_1$ with
everything in $E_\infty^{0,*} = Z(A)$. Its own proof block draws the practical
conclusion explicitly:

> *No higher-page differentials $d_r$ ($r \geq 1$) need ever be computed — they
> all vanish.*

That is mathematically unobjectionable for the **finite** Hecke algebra at
generic $q$ (Whitehead's lemma for separable algebras). Taken as a tool it says:
the only data available is $\{\chi_\lambda(\rho(\beta))\}$, one number per
partition. That is precisely the form
$B = m_e \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$ that is already
known to fail — and the failure is not marginal. The
[⁴He measurement](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md)
exceeds the complete-graph pairwise ceiling by $11.12$ MeV.

**So if the collapse holds, it is the first candidate proved invariant for a
scope-(b) exclusion of "look harder inside $H_n(q)$".** That is a real use — it
just is not the use the question was hoping for.

## 2. Three reasons the collapse is not established

**(a) The Lean proves a different proposition.** `QOU.WedderburnMass.spectral_sequence_collapses_to_centre`
has conclusion

```lean
∀ i : I.central_idempotents, I.e i * I.e i = I.e i
```

and body `fun i => I.e_idem i`. It projects a class field. It does not mention
$E_\infty$, does not mention a filtration, and **never uses its own
`[WhiteheadHH R A]` instance**. The docstring above it states the $E_\infty$
result. This is the §3b-cond item-5 shape — a class field re-exported as a
theorem — and the block's `.ts` carries `validation: "not_checked"`.
**It is not in [`lean-vacuity-review-ledger.json`](lean-vacuity-review-ledger.json)**,
so no agent verdict has ever been recorded against it.

**(b) `WhiteheadHH` is a conjectural class.** Mathlib has no Hochschild-cohomology
framework; the file says so. That is honest and is not the defect — (a) is.

**(c) The filtration whose collapse is asserted is not defined.** Per
[`2026-08-16-three-gb-filtrations-one-name`](2026-08-16-three-gb-filtrations-one-name.md),
the corpus calls three inequivalent objects $J^\bullet$ and each is excluded:

| reading | disposition |
|---|---|
| ideal-power $\pi(I)^k$ | provably $\bot$ for $k \geq 1$ — `QOU.BraidKnot.WordFiltration.map_pow_eq_bot`, sorry-free |
| Coxeter length | well defined, but fails a dimension count at $n \leq 3$ |
| rewrite depth | identically zero once `def:hecke-normal-form` fixes $T_w$ as the unique NF basis |

A spectral sequence needs a filtration. There is no agreed one.

## 3. The extensive term already exists — on the *jet* filtration

This is the part that answers the gap.
[`conj:binding-manybody-eq-jet-filtration`](../../content/quantum-observable-universe/mass-theory/binding-manybody-jet-filtration.md)
gives the binding as a **body-order series**

$$
  B(K) \;=\; \sum_{n \geq 2} m_e\, a_D^{(n)}(K),
  \qquad
  a_D^{(n)} \;=\; \oint_{\mathcal{S}_c} \lambda_{\mathrm{SW}}^{(n)} ,
$$

and [`prop:jet-filtration-binding-extensive`](../../content/quantum-observable-universe/mass-theory/jet-filtration-binding-extensive.md)
proves — sorry-free, elementarily — that this is **extensive**: monotone in the
body-order cutoff $A$, strictly increasing whenever a new body order contributes.

**That is exactly the object the ⁴He measurement demands**: a super-pairwise,
additive, extensive term. It is not missing from the corpus. Its *shape* is
right and its *magnitude* is open, and the block says so, carrying three named
open inputs — the Seiberg–Witten period magnitude, the non-abelian-Stokes
identity $a_D^{(n)} = \mathrm{lw}(n-1)$, and the residue weight $w_n(K)$.

**The jet filtration and the GB filtration are different objects.** The GB one
filters $H_n(q)$ at fixed $n$; the jet one indexes the tower over body order.
Collapse of the first says nothing about the second.

## 4. NEW: the binding chain routes through the unestablished bridge too

Bean `wpdb` lists five consumers of the word-depth $\to$ partition-depth bridge,
and all five are **mass-formula** sites. There is a sixth, and it is on the
**binding** side:

```text
prop:jet-filtration-binding-extensive        (extensive, sorry-free)
  -> conj:binding-manybody-eq-jet-filtration
       -> lem:bond-order-eq-jet-degree       ("body order n = jet degree n")
            -> prop:gb-spectral-sequence
            -> prop:jet-prefix-gb-filtration
```

and `prop:jet-prefix-gb-filtration` **defines** its jet prefix as a GB-filtration
graded piece:

$$
  \beta_k^{\mathrm{GS}} \;:=\; \sigma_{k-3}(T_w) \;\in\; J^{k-3}(q) / J^{k-2}(q).
$$

So the identification of body order with jet degree — the step that says *which*
$a_D^{(n)}$ belongs to an $n$-nucleon cluster — is stated in terms of the same
$J^\bullet$ that has three excluded readings.

**Two consequences worth stating separately, because one is much weaker than the
other.**

*The strong one, and it is only a consistency observation:* under the
ideal-power reading, $J^{k-3}/J^{k-2}$ is the zero quotient for every $k > 3$,
so every $\beta_k^{\mathrm{GS}}$ above the first stratum vanishes and the
body-order series would truncate at the pairwise term. That is the same shape as
the measured ⁴He failure. **This is not a derivation and must not be reported as
one** — the ideal-power reading is the one already *excluded*, so its
consequences are consequences of a reading nobody is committed to. What it shows
is that the two candidate explanations are not obviously independent.

*The weak one, which is solid:* the magnitude gap is **not** downstream of
$J^\bullet$. $a_D^{(n)}$ is a Seiberg–Witten period; the GB filtration enters
only the *indexing*. So fixing $J^\bullet$ would not by itself supply the
missing MeV — it would tell you which term they belong to.

There is also a degeneracy that lands directly on the light isotopes. The atom
word sits in $H_{3A}(q)$, and `QOU.BraidKnot.gbDepth_const_on_H3` (sorry-free)
shows `gbDepth` is **constant** on the partitions of 3. At $A = 1$ the grading
the chain reads off is degenerate, and it first separates at $n = 4$.

## 5. The ingested literature — one direct hit, unmined, and it cuts the other way

`grep -in "spectral sequence" library/INDEX.md` returns **nothing**: 332
documents, no spectral-sequence source. `filtration` likewise returns nothing.
`Hochschild` returns exactly one, and it is the right one.

**[`arxiv-1108.5286v3`](../../library/arxiv-1108.5286v3/) — Solleveld,
*Hochschild homology of affine Hecke algebras*.** Registered in the bib as
`solleveld2022` with the library dir wired. **Cited by zero content blocks.**
Its §3.1 gives, for the affine Hecke algebra,

```text
  HH_*(H ⋊ Γ)  ≅  ⊕_{w ∈ ⟨W'⟩}  Ω^*(t_{ρ_w})^{G_{ρ_w}}
```

— algebraic differential forms of **every** degree on the extended quotient of a
torus by the Weyl group, independent of $q$, via Morita invariance and
Hochschild–Kostant–Rosenberg.

**This does not contradict the corpus.** Finite $H_n(q)$ at generic $q$ is
semisimple and its higher $HH$ genuinely vanishes; Solleveld's algebra is
affine. What it establishes is the *scope* of the corpus's no-go: the vanishing
is a property of finiteness, not of Hecke algebras. Higher Hochschild **homology**
survives once one leaves the finite algebra — and the corpus has an
inductive-limit tower to leave it into
([`markov-trace-inductive-limit`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-inductive-limit.md),
whose Lean already names *"the infinite-dim affine Hecke algebra"* as open R&D).

The suggestive part, offered as a lead and nothing more: Solleveld's classes are
indexed by conjugacy classes of $W$ — for type A, partitions again — but valued
in $\Omega^j$, a **de Rham degree** the finite centre does not have. A grading by
form degree over a partition index is the shape the body-order series wants. It
is a shape match, not an identification, and the specialization has to be
exhibited rather than asserted.

### The gates, checked 2026-08-25

Three, not the two this note first listed. **(i) and (ii) pass; (iii) is mine and
is unresolved.**

**(i) Parameter regime — passes.** Solleveld's §1.1 defines *equal* parameters
($q(s)$ constant on $S_{\mathrm{aff}}$) and *positive* parameters
($q(s) \in \mathbb{R}_{>0}$). "Possibly unequal" in the abstract is a
*generalisation*; equal is the special case. The corpus sits at a single real
$q_0 \approx 1.10998$ — positive, and not a root of unity. Nothing here excludes
it.

**A convention trap sits inside that gate, and it is the expensive kind.**
Solleveld's Hecke relation (§1.1, eq. 2) is

$$
  \bigl(N_s - q(s)^{1/2}\bigr)\bigl(N_s + q(s)^{-1/2}\bigr) = 0 ,
$$

against the corpus's $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ (AGENTS.md §7a). So
**Solleveld's $q$ is the corpus's $q^2$** — his $q^{1/2}$ is our $q$. At the
substrate anchor that is $q_{\mathrm{Sol}} = q_0^2 \approx 1.23206$, not
$1.10998$. He notes himself that the literature also defines the algebra via
$q(s)^{1/2} N_s$. Any numeric transfer that skips this is off by a square root,
which is the same shape as the convention-C/D confusion the corpus has spent
months draining.

**(ii) The 2022 correction — does not block, with a hedge.** It lands in §2.1 and
§2.2 (pages 16–22), on the construction of families of representations, and it
does reach §3.1, which picks its families *"as in Corollary 2.5"*. But Solleveld
supplies the repair in the same note: families satisfying Lemma 2.3 can be found
when the parameters are of *"geometric type"* (via [AMS, §3.3]), and *"for most
positive-valued $q$ one can use the technique with parameter deformations from
[Sol4, proof of Lemma 6.4]"* — after which *"the remainder of the paper is valid
without further changes."* The corpus is positive-valued, so it is inside the
rescued regime. Two hedges to carry: **"most"** is not "all", and **"geometric
type" is undefined in this paper** — it occurs exactly once, in the correction
itself, pointing outward to [AMS]. *(My own reading, not read off the page: type-A
equal-parameter affine Hecke algebras are the Kazhdan–Lusztig / Steinberg-variety
case and should be geometric type — which would make the first bullet apply
directly and the deformation unnecessary. Confirm against [AMS §3.3] before
relying on it.)*

**(iii) Homology is not cohomology — checked, and it SPLITS the lead in two.**
`prop:spectral-sequence-collapse` is about $\mathrm{HH}^k$ (**co**homology).
Solleveld computes $\mathrm{HH}_*$ (**homology**). For a separable
finite-dimensional algebra both vanish above degree $0$, so §1 is unaffected —
but non-vanishing of $\mathrm{HH}_*$ does **not** formally imply non-vanishing
of $\mathrm{HH}^*$ in infinite dimension.

**Read for a bridge; there is none.** Across §3, §3.1 and §3.3 the string
`HH^` never appears, no duality or Poincaré statement is made, and the only
occurrence of "cohomology" is about *cyclic* homology of smooth commutative
algebras. Theorem 3.1 is proved at the **complex level**, in the Hochschild
*chain* complex $C_n(A) = A^{\otimes n+1}$ with boundary $b_n$, by exhibiting
representative **cycles**: *"every element of $\mathrm{HH}_*(H \rtimes \Gamma)$
can be represented by a Hochschild cycle in
$\bigoplus_{w} {}^{w}C_*(\mathcal{O}(t_w))$."* The cochain complex
$\mathrm{Hom}(A^{\otimes n}, A)$ has no automatic dual of that step. **So the
cohomological statement is not a transport — it is a separate piece of work.**

*(Not from the page — my own reading, so do not cite it as the corpus's: for the
smooth commutative local model $\mathcal{O}(t)$ that HKR governs here, both
sides are non-zero in higher degrees — $\mathrm{HH}_n \cong \Omega^n$ and,
by the standard cohomological counterpart, $\mathrm{HH}^n \cong \wedge^n
\mathrm{Der}$. So there is no a-priori obstruction; the expectation is that the
cohomological statement also carries higher degrees. Expectation, not result.)*

**Why this splits the lead.** The two readings of Solleveld have different
exposure to this gate:

| reading | needs $\mathrm{HH}^*$? | status after gate (iii) |
|---|---|---|
| *scopes the corpus's no-go* — "the vanishing is a property of finiteness" | **yes** — the corpus claim is cohomological | **weakened.** Bounds the scope only if the dual statement holds, which is unproved |
| *supplies a graded home for the body-order series* | **no** — any extra grading serves | **untouched.** Homology carries the $\Omega^j$ degree regardless |

The second was the interesting half, and it survives intact. State the first with
the qualifier.

**A bonus from reading the proof:** Theorem 3.1's own hypothesis is
*"there exists $\epsilon \in \mathbb{C}^\times$ such that $k_\alpha \in
\epsilon\mathbb{R}$ for all $\alpha \in R$"* — real parameters up to scaling.
The corpus's real positive $q_0$ gives real $k$, so the hypothesis holds. That
independently reinforces gates (i) and (ii).

`arxiv-0911.4494v2` (Webster–Williamson, *The geometry of Markov traces*) is the
other cohomological source and is **already scoped** in the 2026-08-21 lead
above, with four open verification items. Nothing here changes that assessment;
this note does not re-open it.

## 6. What this note does not claim

It does not claim the collapse is false, that the bridge is false, that the
body-order series is wrong, or that Solleveld's classes are the missing term. It
claims: the collapse is a no-go rather than a tool; its Lean proves something
else; the binding chain is a sixth consumer of an unestablished bridge that bean
`wpdb` tracks only on the mass side; and one directly-relevant ingested source
has never been read into the corpus.
