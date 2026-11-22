# The atom-word closures are not hyperbolic — so the volume route cannot justify `B_sym`

**Date:** 2026-08-25 · **PR:** [#5765](https://github.com/litlfred/qou/pull/5765) ·
**Beans:** `qou-2pnv`, `qou-d5e8`, `qou-9ot5`

Follows the owner's suggestion — *"we have proved special cases of the vol conjecture …
we can try to prove all needed for qou potentially"*. The strategy is sound and **works
for the anchors**. For the atom words it returns the opposite of what was wanted: KVC
there is **not open — it is proved, and it proves `Vol = 0`.**

SnapPy 3.3.2 was installed in-sandbox and every hyperbolicity statement below is
**computed, not recalled** (fig-8 = 2.0298832128 ✓ against `2·Cl₂(π/3)`).

## 1. The owner's discharge succeeds for Class A

Authoritative in-corpus list: H. Murakami, *An introduction to the volume conjecture*
§3.3, [`library/arxiv-1002.0126v1/sections/sec-007-3-volume-conjecture.md`](../library/arxiv-1002.0126v1/sections/sec-007-3-volume-conjecture.md) lines 431–447.

| QOU knot | Vol | Role | KVC |
|---|---|---|---|
| **4₁** | 2.0298832128 | **CAL-2 muon anchor** — q₀ itself, 147 sites | **PROVED** §3.3(1) Ekholm |
| **L6a4 Borromean** | 7.3277247534 | nucleon / `F_Bor` | **PROVED** §3.3(7) Garoufalidis–Lê |
| **5₂** | 2.8281220883 | lepton/Bring ladder | **PROVED** §3.3(2) Kashaev–Yokota |
| **6₂** | 4.4008325161 | deuteron knot-ID | **PROVED** Ohtsuki–Yokota Thm 1.1 (`library/ki6c/`) |
| Hopf, T(2,3/5/7) | 0 | photon, leptons | **PROVED** §3.3(4)(5)(6) |
| **8₁₁** | 8.2863168178 | triton knot-ID | **OPEN** — absent from §3.3 |
| **7²₁ (L7a6)** | 4.7494999819 | α–α coupling | **UNVERIFIED** — is it a twisted Whitehead link, §3.3(8)? |

**The three load-bearing anchors are all proved.** The 6₂ citation was cross-checked
numerically: the paper's ς(6₂) = 0.700414… gives `2π·Re ς = 4.400831` against SnapPy's
4.4008325 ✓.

## 2. The atom words are a different object, and that is the whole problem

**`atom_braid_word_3A` does not return a braid word.** Each letter is a triple
`(c, d, g)` meaning `c·σ_g + d·1` — an element of `H_n(q)`, not of the braid group. Under
the repo's convention `σ⁻¹ = σ − h`, the averaged crossings are **exactly** weight-1
averages over crossing sign:

```
σ − (h/2)·1        = ½σ + ½σ⁻¹
σ − h(½ − δ/4)·1   = (½+δ/4)σ + (½−δ/4)σ⁻¹
```

For ²H: 11 letters `σ`, 7 letters `σ⁻¹`, and **5 non-braid** (4 intra-nucleon averages +
1 p–n colour-weighted) — exactly `2A+1` in general, since each nucleon contributes two
`ud` pairs plus one interface.

So by linearity `tr_M(W)` is a weighted sum of **2^(2A+1) = 32** link invariants for ²H.
**There is no single closure to ask KVC about.**

| isotope | strands | letters | non-braid | branch braids | closure components |
|---|---|---|---|---|---|
| ²H | 6 | 23 | 5 | **32** | 3 |
| ⁴He | 12 | 47 | 9 | 512 | 5 |
| ⁷Li | 21 | 83 | 15 | 32768 | 8 |

## 3. Every branch closure is non-hyperbolic — four steps, each verified

1. **Each branch braid is monotone** — one run per generator. Verified
   `one-run-per-generator = True` for **every (Z,N) with A = 2…24**, and structural by
   construction (nucleon *k* writes generators 3k, 3k+1, 3k+2 in ascending order, once
   each). The repo already calls this a "monotone braid" and exploits it for the `B_sym`
   closed form — without drawing the topological consequence.
2. **Hence the closure is a connected sum of (2,k) torus links**, `#_g T(2, e_g)`.
   **Verified against SnapPy `deconnect_sum` on 32/32 branches, zero mismatches** —
   predicted multiset of (crossings, components) matched observed every time. All 32
   give 4 non-trivial summands from {Hopf, T(2,4), T(2,3), T(2,5), T(2,7)}.
3. **Connected sums are non-prime, hence never hyperbolic** (Thurston); **(2,k) torus
   links are Seifert-fibered**, so `Vol = 0`.
4. **SnapPy confirms independently:** 32/32 branches fail to find a geometric solution
   across 30 randomised retriangulations, all reporting degenerate tetrahedra with
   volume ~1e-4 noise.

This **reproduces and extends** [`2026-07-04-he4-link-volume-braid-closure-refuted.md`](2026-07-04-he4-link-volume-braid-closure-refuted.md),
which already found the proton, neutron, ³H, ³He and ⁴He closures non-hyperbolic
numerically. **Not claimed as new.** New here: **²H**, the exact structural reason, and
the branch expansion.

## 4. The inconsistency, stated precisely

KVC's convention makes the RHS vanish on non-hyperbolic links, and **van der Veen
§3.3(6) proves KVC for volume-zero links**. So for the atom words KVC is **discharged**
— and yields **0**. Measured at 50 dps:

```
tr_atom(2H)          = 0.57517224391777187083
tr_free(2H)          = 1.13171690432221008273
ln(tr_free/tr_atom)  = 0.67682159238634338966     != 0
B_sym(2H)            = alpha * 0.676822 = 2.833 MeV
```

**`Vol = τ_arch(Vol_q)` demands 0 where the pipeline uses 0.6768.**

The corpus's own lemma says the same by the same argument —
[`degree-one-braid-trivial-volume-proof.md`](../content/quantum-observable-universe/mass-theory/degree-one-braid-trivial-volume-proof.md):

> *"Mass generation requires a closure that is genuinely hyperbolic… Any candidate
> constructed as a degree-one element of the Hecke algebra is automatically
> volume-trivial, hence cannot acquire mass through the τ_arch ∘ Vol_q pipeline."*

The atom word is degree ≥ 2 so that lemma does not literally apply — but its
**invariant** (non-hyperbolic ⇒ Vol = 0 ⇒ no mass) does, and the non-hyperbolicity it
requires is now proved.

**A one-block fix would have caught this:** `vol-through-tau.md` states its proposition
*"for every braid β ∈ H_n(R,q)"* — conflating a **braid** with a general **Hecke
element**. The atom word is the latter. Tightening that quantifier is cheap and correct.

## 5. What this does NOT touch

- **The binding numbers stand.** `B = −α·ln|tr_M|` as a *formula* is untouched; it needs
  a different derivation than the volume route.
- **The Class-A anchors are untouched** and are now largely discharged (§1).
- **The canonical-knot-ID route is untouched and looks healthier.** Verified
  independently this session:

  | route | ²H binding | error vs AME |
  |---|---|---|
  | `m_e·Vol(6₂)` (knot-ID) | **2.248820798 MeV** | **+1.09 %** |
  | production `B_sym` (Markov closure) | 2.832825 MeV | +27.34 % |

  That route assigns links by **Jones-polynomial identification**, not by Markov closure,
  so it is not affected by §3. **It is a postdiction on one nucleus with an assignment
  that itself rests on the open `conj:canonical-knot-id-sdp`** — it is not a win, it is a
  lead. The 2026-07-04 audit already recorded that the two routes disagree.

## 6. Scope

**Scope-(b), structural exclusion**, invariants named: (1) the one-run-per-generator
normal form, verified for all A ≤ 24 and structural by construction; (2) the closure
identity `#_g T(2,e_g)`, verified 32/32 against SnapPy; (3) connected sums are non-prime
hence non-hyperbolic; (4) (2,k) torus links are Seifert-fibered.

The excluded claim is narrow: **the Markov closure of `atom_braid_word_3A` cannot supply
a nonzero hyperbolic volume, so KVC cannot be the justification for `B = −α·ln|tr_M|` on
the atom words.**

## 7. What remains

| # | item | status |
|---|---|---|
| 1 | cite §3.3 per-knot and discharge the class hypothesis for 4₁, Borromean, 5₂, 6₂, torus/Hopf | **bookkeeping** — the owner's idea, ready to execute |
| 2 | **7²₁ (L7a6)** — twisted Whitehead? | cheap, hours |
| 3 | **8₁₁** | genuine research; Ohtsuki's machinery stops at 6 crossings. A paper |
| 4 | **the atom-word justification** | **the real work**, and not a KVC problem |

For item 4, three options, none adjudicated here: **(a)** accept `Vol_alg := tr_M` as
primitive, drop the `vol-through-tau` justification for the binding forms, and derive
`B = −α·ln|tr_M|` some other way; **(b)** route binding through the knot-ID assignment
(6₂, 8₁₁, …), making items 2–3 the live gate; **(c)** replace the averaged interfaces
with genuine braid letters so a single closure exists — but that changes `tr_M` and every
binding number, so it is not free.

## Incidental

`KnotRegistry.lean:114` documents 4₁ as *"Exact: 3 · Cl₂(π/3)"*. Per AGENTS.md that name
is wrong (correct: `2·Cl₂(π/3) = 6Λ(π/3)`); the value beside it, 2.02988321281931, is
right — the wrong-name/right-value class AGENTS.md warns about. Tracked under `qou-zdz5`.


---

## Addendum 2026-08-25 — this is an instance of Nielsen–Thurston, not an accident

The library ingest surfaced **Ito, *Braid ordering and the geometry of closed braid*
(arXiv:0805.1447v2)**, now at [`library/arxiv-0805.1447v2/`](../library/arxiv-0805.1447v2/).
It reframes the result above.

**Verified in the ingested text** ([`sec-006-5-nielsen-thurston-classification…`](../library/arxiv-0805.1447v2/sections/sec-009-5-nielsen-thurston-classification-and-the-geomet.md)):
every braid is exactly one of **periodic**, **reducible**, or **pseudo-Anosov**, and

> *"F admits a complete hyperbolic structure **if and only if** φ is pseudo-Anosov"*, while
> *"F_φ is **Seifert-fibered** if and only if φ is **periodic**"*, and a **reducible** φ gives
> a complement containing an essential torus, hence decomposable.

**So the measurement above is the classification, restated.** Each branch braid is monotone
⇒ its closure is a connected sum of (2,k) torus links ⇒ **periodic/reducible, never
pseudo-Anosov** ⇒ non-hyperbolic. The SnapPy failure on 32/32 is not a numerical accident;
it is what Nielsen–Thurston predicts for that class of word.

Two consequences worth having:

1. **The question becomes decidable in general.** "Is this closed braid word hyperbolic?"
   is a Nielsen–Thurston classification of the word — algorithmic — rather than a
   per-isotope SnapPy experiment. Any future atom word can be classified without
   triangulating anything.
2. **A candidate structural reason, not just a fact.** Ito's classification theorem carries
   a **Dehornoy floor ≥ 3** hypothesis, and short atom words have *small* floor — precisely
   the regime where a word admits many closed-braid representatives and closures tend to be
   torus or composite. That suggests the non-hyperbolicity is forced by the *shortness and
   monotonicity* of the interface construction, not by the choice of interface element.

> **Scope of what I verified.** I read the Nielsen–Thurston trichotomy and the
> hyperbolic ⟺ pseudo-Anosov / Seifert ⟺ periodic statements **directly in the ingested
> text** — those are confirmed. I did **not** locate the `[β]_D ≥ 3` hypothesis or confirm
> the "Theorem 2" numbering by grep; that part is **reported, not verified here**, and item
> 2 above is a **conjecture about why**, not a result. Treat it as a lead.

> **Follow-up on item 2 (2026-08-25, different session).** The lead was taken up
> and the premise now measured: corpus floors are 0–1, and the smallest braid
> reaching floor 3 is `Δ⁶` — 18 crossings. But the **implication runs the other
> way**. Ito's Proposition 4 (*"`β̂` a non-braided satellite knot ⇒ `[β]_D < 3`"*)
> and Remark 4 (Menasco–Nakamura: *"closure composite ⇒ `[β]_D < 2`"*) give
> **composite ⇒ small floor**; item 2 uses the converse, and the converse fails —
> `4₁` is prime, hyperbolic, and has floor **0** across 118 097 conjugates at
> minimal braid index. A small floor is a fact about **scale**, not about
> geometry. The `[β]_D ≥ 3` hypothesis and the Theorem 2 numbering are now
> **verified** in the ingested text, as is the mapping-torus/closure distinction
> the scope note was right to be cautious about. **Item 1 and the primary
> conclusion are untouched** — they rest on monotonicity, and Proposition 4 read
> forwards supports them. Full working:
> [`2026-08-25-ito-dehornoy-hyperbolicity-criterion.md` §Addendum 3](2026-08-25-ito-dehornoy-hyperbolicity-criterion.md).


---

## Addendum 2026-09-07 — §3 is true of the GROUPED word and stale for the live one; the connected-sum half survives, the Vol = 0 half does not

Bean `qou-m6gp`; producer
[`binding_volume_difference_probe.py`](../../computations/probes/binding_volume_difference_probe.py)
(leg C, evaluated for the first time on 2026-09-07 — until then its SnapPy
helper returned `(None, None, False)` on `ImportError` and the leg had never
run).

**What changed underneath §3.** Step 1 ("each branch braid is monotone") relied
on the per-nucleon confinement core being laid down grouped (`σ₀³ σ₁⁻³`). Bean
`qou-hu1f` (2026-09-05, owner ruling) made the core alternating, `(σ₀σ₁⁻¹)³`,
which is not monotone — `σ₀` recurs. So steps 1–2 no longer apply to the live
word, and the measurement was repeated rather than inherited.

**Measured on the live word, SnapPy 3.3.2, ManifoldHP (quad-double, unverified —
`verified=True` needs Sage):**

| nucleon | branch signs | closure | components | Vol |
|---|---|---|---|---|
| proton | (+,+) | L9n10 | 2 | 9.9665118837 |
| proton | (+,−) | L11a252 | 2 | 16.1911429640 |
| proton | (−,+) | L7a6 (= 7²₁) | 2 | 4.7494999819 |
| proton | (−,−) | L9a21 | 2 | 11.9428724495 |
| neutron | (+,+) | L11a252 | 2 | 16.1911429640 |
| neutron | (+,−), (−,+) | L9a21 | 2 | 11.9428724495 |
| neutron | (−,−) | L11n202 | 2 | 8.1957030826 |

Every per-nucleon branch closure is **hyperbolic** (all tetrahedra positively
oriented, census-identified). The 2H "Vol = 0 for every one" of §3 is therefore
**retracted for the live word**; it stands as a record of the grouped one.

**What survives, and it is the load-bearing half.** Each inter-nucleon interface
is a single letter, so `closure(β₁·σ_k^±·β₂) = closure(β₁) # closure(β₂)`:
`deconnect_sum` on all **800** atom branches (32 + 128 + 128 + 512 for
²H/³H/³He/⁴He) returns exactly `A` summands, every one matched to the table
above. A connected sum is non-prime hence non-hyperbolic (0/800 whole closures
find a geometric solution), and the simplicial volume of a link exterior is the
sum of the hyperbolic volumes of its JSJ pieces (Gromov; Soma), the JSJ pieces of
a connected sum / split union being those of the summands, so

```
Vol(atom branch) − Vol(free branch) ≡ 0      (max over 800 branches: 2e-63, summation rounding at 70 dps)
```

for every branch, every weighting, and every ρ: the volume-DIFFERENCE binding
`B_C = ρ·[Vol(atom) − Vol(free)]` is **0**, residual −100 % on all four nuclei.
That is scope-(b) with the invariants named (single-letter-interface closure
identity; connected-sum additivity of simplicial volume), and it is narrower than
§6: it excludes a *difference* reading, not a volume reading. An absolute-volume
reading (branch volumes 12.9–64.8, weight-averaged 22.78 / 34.85 / 33.49 / 45.56
for ²H/³H/³He/⁴He), a non-additive functional of the pieces, or a multi-letter
interface are **not** excluded here.

**Consequence for §4–§6.** The KVC "discharge to 0" argument of §4 depended on
the branch closures being non-hyperbolic; on the live word they are not, so §4
does not go through as written — the atom object is still a weighted sum of 2^(2A+1)
link invariants with no single closure (that part is unchanged), but the
per-branch volumes it averages are now nonzero. Option (c) in §7 ("replace the
averaged interfaces with genuine braid letters") is unaffected; option (a)/(b)
should be re-read against the table above.
