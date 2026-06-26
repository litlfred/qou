# T2/T3 trace-invariance — status synthesis and the precise open question

**Date:** 2026-06-26
**Branch:** `claude/t2t3-trace-invariance-synthesis-2026-06-26`
**Status:** Synthesis audit. Consolidates the scattered T2/T3 + brane-tower
+ isospin findings into one current status with re-verified magnitudes, and
pins the open derivation question precisely. **Nothing wired**; this is a
framing/triage doc, not a production change.
**Scope discipline:** the negative below is **(b) structural exclusion** with a
cited invariant (the Markov axiom $\mathrm{tr}_M(\sigma_i)=z$ is reduced-word
independent); the accuracy gap is **(a) scope-limited** (a construction misses
the numbers, not an ingredient ruled out). Per AGENTS.md §"Before declaring
refuted".

## TL;DR

The six-term mass formula
([`knot-mass-formula-unified`](../../content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.md),
[`six-term-mass-formula-complete`](../../content/quantum-observable-universe/mass-theory/six-term-mass-formula-complete.md))
requires every term to be a **Markov-invariant trace**. Terms 1, 4, 5, 6 satisfy
this. Terms 2 and 3 (the brane tower) sit on a **dilemma**, not a missing step:

- The **trace-invariant** form $\sum_S z^{|S|}\mathrm{Vol}_q^{(S)}(\beta)$ has the
  universal closed form $T_2=(n{-}1)z^2$, $T_3=\binom{n-1}{2}z^4$ — it depends
  **only on the strand count $n=3A$**, hence is **isospin-blind**: any two
  isobars (same $A$) receive *identical* $T_2,T_3$. It carries **zero**
  mirror-splitting. *(b)-exclusion: Markov axiom ⇒ word-independent.*
- The **production** $\Phi_q(|\hat V_i^{\mathrm{full}}|)$ form (the archimedean
  Kashaev specialisation) carries per-generator structure — but it is
  basis-dependent (not a trace), it amplifies tiny p/n asymmetries by $\sim10^5$
  at $q_0$, and its bounded $-\mathrm{Li}_2^q$ variant **inverts the Z-ordering**
  of the mirror pair (`2026-06-18`).

**The open derivation question is therefore not "make T2/T3 a trace"** (the
R-side form already is one) **but "find the trace form that is *also* the
correct mirror-splitting"** — i.e. reconcile Markov-invariance with the
binding physics. As a corollary, in any *trace* reformulation the entire
T/³He splitting must be carried by $T_1$ (descended $\mathrm{tr}_M$) and $T_5$
(chirality), **not** by the brane tower.

## Re-verified magnitudes (2026-06-26, this branch)

At the canonical muon-$q_0 \approx 1.10998$, $z=1/(q^{1/2}+q^{-1/2})$:

| quantity | value | note |
|---|---|---|
| $z=\mathrm{tr}_M(\sigma_i)$ | $0.499320$ | Markov axiom, word-independent |
| $z^2=\mathrm{tr}_M(\sigma_i\sigma_j)$ | $0.249321$ | Markov pair, [`prop:markov-pair-z2`](../../content/quantum-observable-universe/mass-theory/six-term-per-derivation-weights.md) |
| $T_2{+}T_3$ R-side, $A{=}3$ ($n{=}9$) | $3.7351$ Hecke-u | **identical** for T and ³He |
| $\Phi_q(0.99)$ | $\approx 6.9\times10^5$ | per-generator Kashaev term |

R-side closed form across $A$ (isospin-blind, depends only on $n=3A$):

| $A$ | $n$ | $T_2=(n{-}1)z^2$ | $T_3=\binom{n-1}{2}z^4$ | $T_2{+}T_3$ |
|---|---|---|---|---|
| 1 | 3 | 0.49864 | 0.06216 | 0.56080 |
| 2 | 6 | 1.24660 | 0.62161 | 1.86821 |
| 3 | 9 | 1.99457 | 1.74050 | 3.73507 |
| 4 | 12 | 2.74253 | 3.41885 | 6.16138 |

Contrast: the production per-generator bounded $-\mathrm{Li}_2^q(-|\hat V_i|)$ tower
(`2026-06-18`, exact production $|\hat V_i^{\mathrm{full}}|$) gives
deuteron $3.393$, tritium $5.072$, ³He $5.350$ — i.e. it *does* distinguish the
mirror pair, but with $\text{tower}(³\text{He})>\text{tower}(\text{T})$, the
**wrong sign** (³He is the *less*-bound member).

## Where each known result sits

| Doc | Contribution |
|---|---|
| [`2026-05-03-T2T3-derivation-chain-analysis`](2026-05-03-T2T3-derivation-chain-analysis.md) | The derivable trace-invariant form is the **GB-residue spectral sum** $r_\ell=\mathrm{Res}_{\zeta_\ell}[\Phi_q\cdot\mathrm{tr}_{M,\ell}]/(q_0-\zeta_\ell)$; the literal $\Phi_q(|\hat V_i|)$ is its Kashaev specialisation (step 5 = where invariance breaks). |
| [`2026-06-18-he3-brane-tower-structural-gap`](2026-06-18-he3-brane-tower-structural-gap.md) | The per-generator tower is **monotone in proton near-pole count** ⇒ predicts ³He *more* bound than T ⇒ **Z-ordering inverted**. |
| [`2026-06-19-bn-bp-brane-tower-parity-obstruction`](2026-06-19-bn-bp-brane-tower-parity-obstruction.md) | Live q-Bessel/Jacobi–Anger **tower-convergence gate**: does the $\chi_\lambda(\mathcal B_n-\mathcal B_p)$ parity residual shrink $n=3\to6\to9$? Blocker: no $H_6/H_9$ explicit p/n braids in corpus. |
| [`2026-06-15-bqclt-isospin-split-coulomb-not-categorical`](2026-06-15-bqclt-isospin-split-coulomb-not-categorical.md) | Mirror isospin split via bond-type composition over-predicts ~2×; a free length scale is the only input. |
| [`2026-05-24-isospin-categorical-source`](2026-05-24-isospin-categorical-source.md) | Isospin = flavour swap $u\leftrightarrow d$; partial crystal-limit formalisation; operator-valued interface extension open. |

## The three candidate trace reformulations (and their status)

1. **R-side algebraic** $\sum_S z^{|S|}\mathrm{Vol}_q^{(S)}$ — Markov-invariant by
   construction; **isospin-blind** (above). Cannot, alone, produce mirror splits.
2. **q-deformed Wedderburn-weighted** $\sum_n c_n\,\mathrm{tr}_M(\sigma_i^n)$
   (Heine identity) — converges to $\Phi_q(z)$, each summand a trace; same
   accuracy ceiling as path 1 in additive variants.
3. **Habiro single-trace** $\sum_m a_m(T_w)\,(u;u)_m/\mathrm{denom}(u)$, $u=q^{1/2}$
   — absorbs $T_2{+}T_3{+}T_6$ into one cyclotomic trace; **empirically sub-1%**
   on $\{p,n,D,T,³\mathrm{He}\}$ with a single-prefactor model
   ([`path-b-habiro-mass-probe.witness.json`](../../computations/probes/path-b-habiro-mass-probe.witness.json),
   $\alpha_M=5.7292$ MeV from deuteron). Its CODATA match is **empirical**;
   deriving it from the categorical identity $\mathfrak m=m_e\rho|\mathrm{tr}_M|$
   is open.

## The precise open question

> Find a **Markov-invariant** trace reformulation of $T_2/T_3$ whose archimedean
> evaluation at $q_0$ reproduces the mirror-nucleus binding **with correct sign
> and magnitude**. Path 1 gives invariance but zero split; the production
> $\Phi_q$ form gives a split but breaks invariance and inverts the sign; Path 3
> gives the right numbers but only empirically. The corollary structural fact —
> that any trace form puts the mirror split entirely in $T_1+T_5$ — is the
> sharpest current constraint and the recommended next formalisation target.

## Item 3 — Path-3 (Habiro) trace-invariance is *automatic*; the gap is the prefactor

Re-examined the Path-3 probe
([`path-b-habiro-mass-probe.witness.json`](../../computations/probes/path-b-habiro-mass-probe.witness.json)).
Two findings:

- **Trace-invariance is not the open part for Path 3.** The Habiro form is
  $\mathrm{tr}_M(T_w)=\sum_m a_m(u)\,(u;u)_m$ — it *is* the Markov trace of the
  braid word, merely re-expanded in the cyclotomic $(u;u)_m$ basis ($u=q^{1/2}$).
  Re-expansion in a fixed basis preserves the value, so Path 3 is Markov-invariant
  **by construction** (unlike the per-generator $\Phi_q$ form). It therefore
  already satisfies the trace-invariance directive; what it absorbs is
  $T_2{+}T_3{+}T_6$ into one trace.
- **The residual open part is the binding prefactor $\alpha_M$, not invariance.**
  The probe's single-prefactor model $B=\alpha_M\cdot|\mathrm{tr}_M^{\text{Habiro}}|$
  uses $\alpha_M=5.7292$ MeV **calibrated from the deuteron**, giving
  p $-0.65\%$, n $-0.56\%$, D $0\%$ (anchor). Deriving $\alpha_M$ from the
  substrate (rather than calibrating it) is the genuine open question for Path 3.
  Note $\alpha_M\approx 5.73 \approx 11.2\,m_e$ — relating it to the
  $E_0$/$m_e$ fibre-functor calibration is the formalize-first target.
- **`α_M` is a calibration, not a derivable number (2026-06-26, formalize-first).**
  The probe's own header declares `α_M` an "acknowledged input, NOT an
  independent calibration" — it is fixed by `α_M = B_D / |tr_M(D)|` from the
  **deuteron**. Asking to "derive `α_M`" as a single substrate number is the
  entropy-bound-forbidden identification the corpus repeatedly warns against
  (cf. the c₃ flip-flop, the A-identification): a lone ~5-sig-fig constant is
  low-information against a basis of substrate constants. A cheap decisive check
  confirms there is **no clean structural match**: `α_M/m_e = 11.21180`, and the
  best single candidate `c_q·q₀ = 11.20266` misses by **~800 ppm** — five orders
  worse than the ~11.5 ppb proton-anchor theory residual, i.e. coincidence, not
  identity. **Do not launch a PSLQ/closed-form hunt for `α_M`.**
- **The genuine open question is structural, not numerical.** `α_M` is the
  binding-sector calibration — the analog of `m_e`/`E₀` for binding energy. The
  real content of Path 3 is that **one** binding calibration (`α_M`, from the
  deuteron) then predicts p, n at sub-1%. The formalize-first question is whether
  the single-prefactor model `B = α_M·|tr_M^Habiro|` is *forced* by the
  categorical identity `m = m_e·ρ·|tr_M|` — i.e. whether `α_M = m_e·ρ_binding`
  for a **derived** (not fitted) categorical density `ρ_binding`. That is a
  derivation target; the bare number is not.
- **Data-integrity flag (not fixed here):** re-running the producer
  `path_b_habiro_mass_probe.py` crashes on the $A\ge3$ rows with an unsubstituted
  free symbol (`-74.0*check_q - 74.0`); the committed witness's $\{p,n,D\}$ rows
  are clean. Tracked as a separate data-integrity item, not in scope for this
  framing PR.

## Item 4 — q-Bessel tower-convergence gate is **already decided**: a parity obstruction

**Correction (2026-06-26, this branch).** An earlier draft of this item said the
$H_6/H_9$ build was "blocked on a first-principles construction, not attempted."
That was **wrong** — corpus-grep caught it. The canonical $A$-nucleon braid
builder `atom_canonical_crossings(A,0,include_inter=False)` **already supports
$A>1$**, and the gate **has been run** at $n=3,6,9$ by
[`bn_minus_bp_brane_tower_parity_probe.py`](../../computations/probes/bn_minus_bp_brane_tower_parity_probe.py)
(witness [`bn-minus-bp-brane-tower-parity.witness.json`](../../computations/bn-minus-bp-brane-tower-parity.witness.json)).
Re-ran it 2026-06-26 — **all assertions PASS, verdict unchanged**:

| level | bar-odd orders | parity | §4a single-$x$ Bessel test |
|---|---|---|---|
| $n=3$ ($A{=}1$) | $\{1,3,5\}$ | **odd** | defined; residual **6.84%**, $x=4.5249$ |
| $n=6$ ($A{=}2$) | $\{2,4,6,8,10,14,16\}$ | **even** | **0/0 undefined** — odd orders $\{1,3,5\}$ vanish ($W_1=0$) |
| $n=9$ ($A{=}3$) | $\{1,3,\dots\}$ | **odd** | (parity flips back) |

The bar-odd **order-parity alternates** odd/even/odd with $A$, and the
conjugation-invariant sign $s=(-1)^{A-1}$ alternates in lockstep. The
Hahn–Exton q-Bessel identification needs a *consistent odd-order* tower
($\sinh((2m{+}1)\eta)$ coeff $=2J_{2m+1}(x)$); at $n=6$ those coefficients
**vanish identically**, so the gate is **structurally obstructed** at the second
rung — this is a **(b)-exclusion** with a cited invariant (order-parity is a
level invariant under the canonical embedding), not a "more compute needed" gap.

**What is actually open is narrower and formalize-first-gated.** The witness's
own conclusion — "a valid brane-tower embedding must preserve odd order-parity"
— is *not* a license to scan embeddings for one that does: the formalize-first
discipline (and the probe's own a-priori-embedding commitment) forbids
scan-to-fit. The genuine residual is to **derive** (not search) whether any
parity-preserving embedding exists from the categorical structure, or to accept
the obstruction as ruling the canonical-embedding q-Bessel tower out. Bean
`t886` is re-scoped accordingly.

## Next steps (owner-selected 2026-06-26, all four)

1. **(this doc)** synthesis + re-verified magnitudes.
2. **Formalize-first** the isospin-blindness of the R-side form as a structural
   (b)-lemma (depends only on $n=3A$ ⇒ zero mirror-split) — prunes the search.
3. **Derive Path-3 (Habiro)** from the categorical identity — close the
   empirical → derived gap.
4. **Push the q-Bessel tower gate** (`2026-06-19`) — construct $H_6/H_9$
   $\chi_\lambda(\mathcal B_n-\mathcal B_p)$; test residual shrinkage.
