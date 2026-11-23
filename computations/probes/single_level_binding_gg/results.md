# Results: single-level binding sum on γγ candidate words (²H, ³H, ³He, ⁴He)

Issue #8983. Preregistration: [`PREREGISTRATION.md`](PREREGISTRATION.md), committed before any
number here was computed. Probe: [`single_level_binding_gg_probe.py`](single_level_binding_gg_probe.py).
Witness: [`single-level-binding-gg.witness.json`](single-level-binding-gg.witness.json), stamped
`q0Anchor: proton`. The final run was
`PYTHONPATH=tools/qou-substrate/python python3 -u computations/probes/single_level_binding_gg/single_level_binding_gg_probe.py | tee …`,
at 70 dps throughout, in about 13 min wall time. The three three-row ⁴He blocks at n = 12 take about 9 of
those minutes, single-threaded.

The `PYTHONPATH` setting matters. Without it, an editable `qou_substrate` installed from another
checkout stamped that checkout's `commitSha` into the witness, and `scriptCommitSha` came out as
`unknown`. Every tabulated number came out the same in both runs.

This is a **probe of a candidate family**, not of ruled words. Scope is (a), per PREREGISTRATION §6:
- the nucleon is `V^m`, `m ∈ {3, 6}`;
- bonds are `V^k`, `k ≤ 3`, at the two straddling vertices;
- the layout is a chain;
- convention D, proton pin.

A negative here excludes nothing outside this family.

## 1. Formula, as computed

`Binding(K) = m_e Σ_{λ ⊢ 3A} y_λ χ^λ(β_K) Δ_λ` and `B_pred := −Binding`, so bound means `B_pred > 0`.
- `Δ_λ = (−1)^{n(λ)} f^λ`.
- `y_λ` is the convention-D weight `y_lambda_su_n(n, q₀, 2)`. It is exactly 0 on every three-row block.
- `χ^λ` comes from the Rust MPFR kernel and is cross-checked against an mpmath seminormal representation.

Secondary reading (§3 item 4): `B_bond := −(Binding(word) − Binding(free word, same m))`.

## 2. Calibration (PREREGISTRATION §4)

| check | result | evidence |
|---|---|---|
| C0 seminormal braid and Hecke relations | pass | max entry error 2.7e-71 |
| C1 kernel vs mpmath, every two-row χ of every row | pass | max relative difference 2.0e-69 |
| C2 `χ_(2,1)(V³)` against the #7741 closed form | pass | 1.994185812979964086728199 by all three routes |
| C3 `tr_M(σ₀) = z_D` | pass | 3.6e-71 |
| C4 Markov property of the restriction | pass | 1.8e-71 |
| C5 `y_λ` two-row formula; three-row `y = 0` exactly | pass | 5.1e-71; exactly 0 |
| **C6** every formation route equals the assembled **ascending** word | **FAIL** | see below |
| C6b (added, reported separately) every route equals an enumerated bond order | pass | normal forms |
| C7 p–n difference at q = 1 and q₀ | pass | words equal; 0 and 0 (see §6) |

**C6 is a falsified preregistered prediction and is left failing.** PREREGISTRATION §1 predicted that
every formation route is, as a Hecke element, the assembled ascending word. That is false for the ⁴He
D+D route `N₀N₁K₀N₂N₃K₂K₁` when the offsets are `(·, 2, 1)`.
- There `K₁` sits on generators {5, 6} and `K₂` on {7, 8}, which do not commute. The D+D route is then
  the **descending** word, not the ascending one. This affects 12 rows: `m ∈ {3,6}`, `k ∈ {1,2,3}`,
  offsets (1,2,1) and (2,2,1).
- Numerically the two are different elements. At `m = 3, k = 3`, offsets (1,2,1),
  `χ_(11,1)` is 10.946437 for ascending and 10.946576 for D+D and descending. The full block list is
  in `formation_routes` in the witness.
- Every route nevertheless has the normal form of one of the two bond orders, both of which were
  already enumerated (C6b). The **row set and every number below are therefore unchanged**. Only the
  stated reason for computing two orders was incomplete: the orders matter for overlapping offset
  pairs, as stated, and the D+D route picks the other one.

The sequential route always equals the ascending word, at both A = 3 and A = 4.

## 3. Results

After dedup by commutation normal form there are:
- ²H: 14 distinct elements out of 26 rows;
- ³H / ³He: 32 out of 50;
- ⁴He: 74 out of 98.

Rows marked `asc,desc` are a single element, because for that offset pattern the two orders commute.

### 3.1 Reading 3 (every level, every two-row μ)

- **Every row with `k = 1` or `k = 2` fails reading 3.** That is ²H 8/8, ³H 20/20 and ⁴He 48/48.
  Failures start at level 3, 4 or 5.
- **Every row with `k = 0` (free word) or `k = 3` passes.** So do both nucleons, `V³` and `V⁶`.

This reproduces at A = 3, 4 the #7741 H₂ pattern that `V³` is the bond power that survives.

### 3.2 Rows that pass reading 3

| nucleus | m | k | offsets | order | Binding (MeV) | B_pred | B_bond | tr ratio vs free |
|---|---|---|---|---|---|---|---|---|
| nucleon | 3 | — | — | — | −0.245745348 | +0.245745348 | — | — |
| nucleon | 6 | — | — | — | −0.241345495 | +0.241345495 | — | — |
| ²H | 3 | 0 | — | — | +0.758291819 | −0.758291819 | 0 | 1 |
| ²H | 3 | 3 | [1] | asc = desc | +0.757534161 | −0.757534161 | +0.000757658 | 0.9984972 |
| ²H | 3 | 3 | [2] | asc = desc | +0.757485884 | −0.757485884 | +0.000805935 | 0.9984972 |
| ²H | 6 | 0 | — | — | +0.745980741 | −0.745980741 | 0 | 1 |
| ²H | 6 | 3 | [1] | asc = desc | +0.746585755 | −0.746585755 | −0.000605014 | 0.9984197 |
| ²H | 6 | 3 | [2] | asc = desc | +0.746444628 | −0.746444628 | −0.000463886 | 0.9984471 |
| ³H = ³He | 3 | 0 | — | — | −1.72449957 | +1.72449957 | 0 | 1 |
| ³H = ³He | 3 | 3 | 5 elements | | −1.71874881 … −1.71869988 | +1.7186999 … +1.7187488 | −0.0057999 … −0.0057508 | 0.99699 |
| ³H = ³He | 6 | 0 | — | — | −1.69420347 | +1.69420347 | 0 | 1 |
| ³H = ³He | 6 | 3 | 5 elements | | −1.6895939 … −1.68946557 | +1.6894656 … +1.6895939 | −0.0047379 … −0.0046096 | 0.99684–0.99690 |
| ⁴He | 3 | 0 | — | — | −0.982611289 | +0.982611289 | 0 | 1 |
| ⁴He | 3 | 3 | 12 elements | | −0.9810575 … −0.9808642 | +0.9808642 … +0.9810575 | −0.0017281 … −0.0015538 | 0.99550 |
| ⁴He | 6 | 0 | — | — | −0.948006826 | +0.948006826 | 0 | 1 |
| ⁴He | 6 | 3 | 12 elements | | −0.9536167 … −0.9528541 | +0.9528541 … +0.9536167 | +0.0048473 … +0.0056098 | 0.99527–0.99535 |

Every row, with all 25+ digits and each block's term, is in the witness under
`results.<nucleus>.rows`.

### 3.3 Rows that fail reading 3 (reported, not adopted)

| nucleus | rows (`k = 1, 2`) | B_pred range (MeV) | B_bond range (MeV) |
|---|---|---|---|
| ²H | 8 | [+0.2762, +0.3145] | [+1.0222, +1.0716] |
| ³H = ³He | 20 | [−0.2944, −0.0565] | [−2.0134, −1.7507] |
| ⁴He | 48 | [−0.6635, +0.0737] | [−1.6189, −0.8743] |

### 3.4 Per-block terms (free word, m = 3)

The sum is a near-total cancellation of large alternating terms, because `Δ_λ` alternates in sign
with the second-row length. For ⁴He (n = 12):

| λ | y_λ | χ^λ | Δ_λ | m_e y χ Δ (MeV) |
|---|---|---|---|---|
| (12) | 0.0039658 | 1 | +1 | +0.0020265 |
| (11,1) | 0.0031003 | 10.976743 | −11 | −0.19129 |
| (10,2) | 0.0023704 | 53.790892 | +54 | +3.51846 |
| (9,3) | 0.0017441 | 153.18743 | −154 | −21.02547 |
| (8,4) | 0.0011941 | 273.25980 | +275 | +45.85198 |
| (7,5) | 0.0006962 | 294.91256 | −297 | −31.15982 |
| (6,6) | 0.0002287 | 131.02605 | +132 | +2.02150 |

These sum to `Binding = −0.98261`. The ²H, ³H and nucleon tables are in the witness.

### 3.5 Three-row blocks (`y_λ = 0`)

Their characters were computed with the same kernel:
- for every row at n = 6 and n = 9;
- at n = 12 for three ⁴He rows: the free word and `k = 3` with offsets (1,1,1) and (2,2,2).

They are **not small**. The maximum `|χ^λ|` is 15.93 at n = 6, 214.69 at n = 9 and 7639.94 at n = 12.
Every one carries `y_λ = 0` exactly (`ocneanuWeight_conventionD_eq_zero_of_three_rows`), so every
three-row term `m_e y_λ χ^λ Δ_λ` is **exactly 0**. There are 182 + 1250 + 210 entries.

Under convention D the single-level sum therefore sees only the two-row (Temperley–Lieb) part of the
word. Whatever the word does on three-row blocks has no effect on `Binding`.

## 4. Diagnostic: the value is almost entirely the identity element

This diagnostic was added after the preregistration. It is reported and was not used to choose
anything.

The same sum on the identity element, where `χ^λ = f^λ`, gives `B_pred(1) = −m_e Σ_{two-row} y_λ (f^λ)² (−1)^{n(λ)}`:

| n | B_pred(identity) | B_pred(free word, m = 3) | identity ÷ free word |
|---|---|---|---|
| 3 | +0.247214813 | +0.245745348 | 100.6 % |
| 6 | −0.762426848 | −0.758291819 | 100.5 % |
| 9 | +1.734692568 | +1.724499570 | 100.6 % |
| 12 | +0.994394167 | +0.982611289 | 101.2 % |

The words move `B_pred` by under 1.2 % from a number that depends only on n. The bonds move it by
under 0.6 % further, which is the B_bond column.

So the **sign pattern of the direct reading** comes from `Σ y_λ (f^λ)² (−1)^{n(λ)}` and not from the
braid word:
- unbound at A = 2;
- bound at A = 1, 3 and 4;
- non-monotone in A (⁴He below ³H).

The reason is that at q₀ ≈ 1.11 the γγ letters are close to the identity in every two-row block. For
example `χ_(2,1)(V³) = 1.994` against `dim = 2`, and the trace ratio of a bonded word to the free word
is 0.995–0.998.

## 5. Outcome classification (PREREGISTRATION §5)

| nucleus | direct reading (`B_pred`) | bond-relative reading (`B_bond`) |
|---|---|---|
| ²H | **(b)**: 6 rows pass reading 3, all with `B_pred < 0` (−0.758 … −0.746) | **(a)**: m = 3, k = 3 rows have B_bond = +0.00076, +0.00081; m = 6 rows are negative |
| ³H | **(a)**: all passing rows have `B_pred` ≈ +1.69 … +1.72, the free word included | **(b)**: every passing bonded row has B_bond < 0 (−0.0058 … −0.0046) |
| ³He | identical to ³H (same word, §6) | identical to ³H |
| ⁴He | **(a)**: all passing rows have `B_pred` ≈ +0.95 … +0.98, the free word included | **(a)**: m = 6, k = 3 rows have B_bond = +0.0048 … +0.0056; m = 3 rows are negative |

No row is ranked or adopted. Where a reading is (a), it is (a) for every passing row of one `m` and
not of the other. The direct-reading (a) cases hold equally for the bond-free word, so they are not
evidence of inter-nucleon binding (§4).

## 6. p–n difference at q = 1 (owner working assumption, PR #8804; bean `qou-az9l`)

Per `qou-az9l`, the q = 1 p–n difference is split into its braid-built part and its α_EM / charge part.

- **Braid-built part: identically 0, at q = 1 and at q₀.**
  - The ³H word (labels p n n) and the ³He word (p p n) are built separately from their labels. They
    are equal as letter strings, because proton and neutron are both `V^m` in this family.
  - Their two-row characters agree exactly: the difference is 0 at q = 1 and 0 at q₀. This was
    computed with the mpmath seminormal representation.
  - The Rust kernel returns `nan` at q = 1, presumably from `h = q − q⁻¹ = 0` in its rescaling; this
    is recorded in the witness and the kernel value was not used. This agrees with
    `FlipSymmetryAtOne` / `FlipSymmetryAtOneBridge`, but trivially so: the family has no flavour.
- **α_EM / charge part: absent.** No candidate carries an α_EM insertion, a charge-squared term or a
  Coulomb term. So the `α·QPair·hol = −m_e/720` non-vanishing of PR #8804 §40 does not arise here.
  The `q_u² = q_d²` condition is not exercised either.
- **Consequence.** The family cannot produce any ³H–³He splitting at any q. It predicts 0 against the
  AME splitting of 8.4817962 − 7.7180413 = 0.7637549 MeV. This was stated in PREREGISTRATION §1a and
  is reported, not repaired.

## 7. Comparison columns, last

The UIC column is the old `unified_iterative_correction(Z, N)` at `K_PARTITION_MAX = 11`, run here.
It is recorded as returned: that producer returns a Python float, and its sign convention is its own.

| nucleus | AME2020 B (MeV) | B_pred, passing rows | B_bond, passing bonded rows | old UIC (K = 11) |
|---|---|---|---|---|
| ²H | 2.2245662 | −0.758 … −0.746 | −0.00061 … +0.00081 | −17.690829002079532 |
| ³H | 8.4817962 | +1.689 … +1.724 | −0.0058 … −0.0046 | −16.333082306143506 |
| ³He | 7.7180413 | same as ³H | same as ³H | −16.0450107923887 |
| ⁴He | 28.2956624 | +0.948 … +0.983 | −0.0017 … +0.0056 | −15.992651004925799 |

Against AME:
- the direct reading is wrong in sign at ²H, about 5× short at ³H and about 29× short at ⁴He;
- the bond-relative reading is three to four orders of magnitude short where it is positive.

As fixed before computing, this is a comparison only. Nothing was selected against it.

The UIC numbers are a different element and a different formula (§8). They are not a calibration.

## 8. Relation to the open owner decision `qou-8274`

`qou-8274` is in progress and is an OWNER DECISION. It asks whether the level-local H₆ = 3A deuteron
word is the right binding object or only the faster one (PR #7202). This probe **does not decide it**.
Related beans read: `qou-w6x3`, `qou-hxz4`, `qou-xkjt`, `qou-sv7h`, `qou-ypq6`.

- **The words differ.** The binding producer's word couples every pair of nucleons: the complete
  graph `K_A`, with `C(A,2)` inter-nucleon letters, inside a fixed `H_k`, `k ≤ 11`. The words here live
  on 3A contiguous strands and can couple only consecutive nucleons, the path `P_A`
  (`QOU/Hecke/ContiguousCouplingGraph.lean::complete_coupling_forces_A_le_two`). The two coincide only
  at A = 2. ⁴He here has 3 bonds against the producer's 6 pairs.
- **The formulas differ.** UIC is a sum over levels k = 2..11 with an underived cap (`qou-xkjt`); this
  probe is the corpus single-level sum at n = 3A.
- **What this probe does supply** to `qou-8274`, for this family:
  - the single-level 3A sum is computable cheaply. Two-row blocks have dimension ≤ 297 at n = 12, and
    the three-row blocks that would hit the `qou-sv7h` O(dim³) wall carry `y = 0`.
  - its value is dominated by a word-independent baseline (§4).
  - reading 3 admits exactly the `k ∈ {0, 3}` bonds.
- Whether that makes the 3A word the right binding object is the owner's question, and this probe
  leaves it open.

## 9. Caveats

1. **Candidate words, not ruled words.** No ruling fixes a γγ word per multi-nucleon nucleus. Nucleon
   `V³ = β_Bor` is a working conjecture.
2. **The direct reading includes the identity baseline.** A nonzero `Binding` for the bond-free word,
   and for a single nucleon (+0.246 MeV), shows that the direct reading does not isolate inter-nucleon
   binding. The bond-relative reading does, but it was not chosen by the corpus. Both readings are
   reported (PREREGISTRATION §0).
3. **The preregistered C6 failed.** The route argument was incomplete (§2). The numbers are unaffected
   because both bond orders were enumerated.
4. **Three-row characters at n = 12 were sampled.** They were computed for 3 of the 74 ⁴He elements, as
   preregistered. Their contribution is exactly 0 for every word by `y_λ = 0`, whatever χ is.
5. **The kernel cannot evaluate at q = 1.** It returns `nan`; q = 1 used the mpmath representation.
6. **Precision.** No float arithmetic was used. The only float is UIC's own return value, which is
   recorded and not used.
