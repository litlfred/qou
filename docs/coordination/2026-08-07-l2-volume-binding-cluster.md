# Coordination ledger — L2 / volume-binding cluster

**Owner branch:** `claude/1ppq-l2-closure-attacks-ufrfun` (PR #4664)
**Opened:** 2026-08-07 · **Skill:** `local/coordinate`
**Session beans:** `qou-kemt` + children

---

## 1. Scope map

| PR | Branch | Scope | Rel. to #4664 | Last active |
|---|---|---|---|---|
| **#4664** (mine) | `1ppq-l2-closure-attacks` | L2 attack options; non-EM binding terms; extended Bloch; volume term | — | active |
| **#4610** | `vol-t-he3-snappy-2026-08-02` | `Vol(T)`, `Vol(³He)` of actual braid closures (SnapPy) | **refutes + supplies** | **5 d stale** |
| **#4591** | `tau-mass-complex-volume-2026-08-02` | `Vol + i·CS` census for m_τ | **constrains** | **5 d stale** |
| **#4640** | `copilot/eight-fold` | eightfold honesty pass; **N=2 obstruction proved** | **refutes A2 premise** | active |
| #4617 | Δ_λ/deuteron μ₃ submodularity | same target (Δ_λ magnitude), distinct route | parallel-OK | active |
| #4658 | 5₂ sum rule, Bloch–Wigner caveat | dilogarithm/Bloch | adjacent | active |

---

## 2. Corrections forced on #4664 by siblings

Recorded per skill §6 — **findings are not silently rewritten**; each is an explicit
retraction with its source.

### 2.1 🛑 A2's premise is REFUTED (source: #4640 §2, §4)

My memo §4 claimed *"the eightfold-way chapter independently argues for `N = 3`."*
**That claim is dead.** #4640 shows the chapter was conflating two different `A₂`s:

| | what it is | where from |
|---|---|---|
| `A₂` of `H₃(q)` | Coxeter type of `W(A₂) ≅ S₃`, permutes **strands** | true **by construction** (`Bₙ` has type `Aₙ₋₁`) |
| `A₂ = 𝔰𝔩₃` | flavour SU(3), acts on the **fibre** `V` | needs `dim V = N = 3` |

*"Setting n=3 does not make N=3"* — and the framework gives **`N = 2`**.

Worse for A2, #4640 §4 **proves** (sorry-free, scope-(b), invariant cited = Schur–Weyl
row cap) that `N = 2` **cannot host** the decomposition: `dim V_{(1³)} = C(N,3)`
vanishes iff `N < 3`; at `N=2`, `8 = 4+4+0` — no singlet, no η′, and *"no choice of q
restores it."*

**Net:** A2 was "test whether binding should use the flavor sector's `N=3`." There is
no flavor `N=3` to import — the framework gives `N=2`, and `N=2` provably cannot host
the octet. That is a **proved open contradiction** (bean `qou-8pl3`, "N=3 routes"), not
a lever available to binding. **A2 → closed as premise-refuted.** The ROAST called it
"near-fatal"; it is now simply dead.

### 2.2 🛑 Hyperbolicity — ESCALATION, not a silent rewrite (source: #4610)

Owner granted caveat 1 this session ("assume it is there and work from there").
**A sibling has already measured it, and the answer is reading-dependent:**

- **Reading 1 — the literal mass-braid `H₉` closures** (`atom_braid_word_3A`):
  **NON-HYPERBOLIC.** SnapPy finds no positively-oriented triangulation under any of
  three averaged-crossing conventions ⇒ **`Vol(T) = Vol(³He) = 0`**. *"The mass-braid
  closure carries no hyperbolic volume."*
- **Reading 2 — corpus-canonical binding links** (SDP registry): `T → 8₁₁`,
  `³He → L6a4 = Borromean`. Both SnapPy-verified **hyperbolic**.

So the owner's grant is **sound under Reading 2 and false under Reading 1**. Escalated
to the author on #4664 rather than picking a reading myself — which reading is
canonical for *binding* is exactly the question, and choosing it to keep my route
alive would be the fit this arc keeps catching.

### 2.3 🛑 `Vol(𝓑₃)` is NOT a per-nucleon volume (source: #4610 Reading 2)

My §5b treated `Vol(𝓑₃) = 7.3277` as the **per-nucleon** volume ("the framework's
nucleon *is* the Borromean link"). The corpus-canonical registry assigns the Borromean
link `L6a4` to **³He — an A=3 isotope**, not a single nucleon. The per-nucleon reading
is withdrawn; §5b's `1.966×` and the factor-2 discussion are recomputed below against
the actual per-isotope assignment.

### 2.4 ⚠️ The CS leg is calibration-blind (source: #4591)

My caveat 2 asked "why would real binding pick up `CS` rather than `Vol`?" #4591 gives
a sharper and more damaging answer: **the muon anchor is CS-blind.** `CS(4₁) ≈ 0`
(figure-eight is amphichiral), so the anchor fixes **no** CS-dependence — *"any
`F(Vol, CS)` reducing to `Vol` at `CS = 0` is equally muon-consistent — a whole
function's freedom."*

**Consequence for the extended-Bloch route:** introducing `CS` as a *magnitude* adds an
unconstrained functional degree of freedom that the calibration cannot check — the same
fit-smuggling in new costume. **The `Vol` leg is unaffected.**

*Distinction worth preserving:* #4591 searches over a free functional `F(Vol, CS)`;
my use of the extended Bloch group is to **fix an integer flattening** from the gluing
equations — that *removes* freedom rather than adding it. So the flattening role
survives; a **CS-carrying magnitude does not**. Route narrows to `Vol` + canonical
flattening.

---

## 3. New result, derived from #4610's own data (cherry-pick candidate)

#4610 concludes *"`ρ = tr_M` radial handle refuted under every volume reading."*
Correct — but their data also shows **what to drop**. Testing the A=3 mirror pair with
**volume alone, zero free parameters** (the overall constant cancels in the ratio):

| quantity | value |
|---|---:|
| `B(T)/B(³He)` (AME2020) | **1.0990** |
| `Vol(T)/Vol(³He)` (#4610 SnapPy) | **1.1308** |
| ratio-of-ratios | **1.0290** → **2.90 % miss** |
| #4610's `Vol·tr_M` prediction | **0.570** vs `C_knot` ratio **1.350** — **anti-correlated** |
| `E₀·Vol/B`: ³He | 3.9743 |
| `E₀·Vol/B`: T | 4.0895 (spread **2.90 %**) |

**Reading:** the refutation in #4610 is a refutation of **`tr_M`**, not of volume.
Dropping `ρ` entirely and using **pure `Vol`** gets the mirror-pair ratio to **2.90 %
with no free parameter**, where `Vol·tr_M` lands on the **wrong side of 1**. The single
overall constant is `≈ 4` for both isobars.

**Discipline flags (stated, not buried):** this is a **two-point** observation on one
mirror pair; `≈ 4` is a constant fitted to two numbers and means nothing until it holds
across `D / T / ³He / ⁴He`; and it is scratch float64, **not witness-grade**
(NO-FLOAT64). The *ratio* claim is the parameter-free part and is the only part worth
anything yet.

---

## 4. Actions taken

- **#4664** — escalation posted (§2.2); memo corrected for §2.1, §2.3, §2.4.
- **#4610** — intent + the §3 volume-only finding posted; **takeover proposed** (5 d
  stale; its own body says *"Lean witness + audit doc to follow"* — never landed).
- **#4591** — intent posted; **takeover proposed** (5 d stale; test plan has 2
  unchecked items: full ≤12-crossing census run + audit doc).
- Beans: `qou-fvzm` (A2) → closed as premise-refuted with #4640 cited.

## 5. Next non-overlapping task

Recompute the volume-binding relation across **all four** L2 binding targets
(`D`, `T`, `³He`, `⁴He`) under Reading 2, ratio-only, zero free parameters — the two-point
`≈4` constant is not evidence until it survives four points. Blocked on the author's
Reading-1-vs-Reading-2 ruling (§2.2).
