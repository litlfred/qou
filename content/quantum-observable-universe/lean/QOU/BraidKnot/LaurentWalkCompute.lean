import QOU.BraidKnot.LaurentWalkDegreeBound

/-!
# A computable Gröbner–Shirshov normal-form walk, with proved semantics

`LaurentWalkDegreeBound` proves the *structural* facts about the walk (degree
growth is linear in the crossing count, multiplying by `h` is a shift). This
file starts the second, larger piece: making the walk itself **executable in
Lean**, so the measured normal-form coefficients are machine-computed rather
than tabulated.

## Why not a tabulation

The obvious way to get the measured degrees into Lean is to write them as a
lookup table and discharge each with `norm_num`. That is exactly the defect
`QOU.AtomicMass.MagicNumbersFromQ` was shown to have — `Phi_signal` tabulates
its own answers, so `Phi_signal_support` had to be added to record that the
positivity of `δ²Φ` at `{8, 20, 28}` is a property of *which entries were
tabulated*, not of the Hecke computation. Repeating that here would produce
theorems that are true, sorry-free, and about nothing.

## What makes a computation trustworthy instead

A computable representation is only worth having if it is *proved to denote*
the abstract object. So the design is:

1. `CLaurent` — a computable Laurent polynomial over `ℚ`, a list of
   `(exponent, coefficient)` terms. No normalisation invariant is imposed:
   duplicate exponents are allowed, because the semantics does not care and
   the invariant would have to be maintained through every operation.
2. `denote` — the `ℚ[T;T⁻¹]` that a `CLaurent` *means*.
3. **Bridge lemmas** — `denote_add`, `denote_mulH`, `denote_smul`: each
   computable operation denotes the abstract one. These are the load-bearing
   content. Without them the executable walk is just a second, unverified
   program that happens to be written in Lean.

Then the walk built from those operations denotes the abstract walk, and
`LaurentWalkDegreeBound.walk_mem_spanRange` applies to it.

## Status — read this before quoting anything from this file

**Proved, sorry-free:** the computable type, its semantics (`denote`), and
all three bridge lemmas — `denote_append`, `denote_csmul`, and the
load-bearing `denote_cmulH`.

**Defined and executing:** the six-component step (`hmStep`), the atom braid
word (`atomNF`), and normalisation (`cnorm`). Running the proton `Z=1, N=0`
through `#eval` gives

    terms per coefficient   [11, 12, 10, 9, 11, 6]
    max q-degree            [10, 11,  9,  8, 10, 5]

which reproduces, exactly, both the Python probe
(`symbolic_nf_q_degree_magic_probe`) and the sympy reference
(`hecke_core_symbolic.build_atom_nf_sym`). Three independent implementations
agree.

**🛑 That agreement is NOT kernel-checked, and the distinction matters.**
`#eval` runs the *compiler's* evaluator, not the kernel, so it is evidence at
exactly the same epistemic level as running the Python — a third program
agreeing, not a proof. Stating `((cnorm (atomNF 1 0 0)).map Prod.fst).max? =
some 10` and closing it with `rfl` FAILS: the kernel cannot reduce it, because
the unnormalised walk builds a 177,045-term intermediate (`rawTerms 1 0`)
before collection leaves 59. `decide` is worse and `native_decide` is banned
outright by the repo's Strict Lean Discipline, so there is no shortcut here.

**Two things are therefore still open, and neither is faked anywhere below:**

1. `denote_cnorm : denote (cnorm a) = denote a` — unproved. Until it lands, a
   degree read through `cnorm` is a computed number, not a proved property of
   the polynomial the walk denotes. No degree is asserted as a theorem in this
   file.
2. Normalising *inside* the step, so the kernel sees ~59 terms rather than
   177,045 and `rfl` becomes feasible. That is what would turn the measured
   degrees into machine-checked claims — and it depends on (1) being proved
   first, or the normalisation would be changing the object silently.

What this file does establish is the harder half: that the computable
operations *denote* the abstract ones. Without those bridge lemmas an
executable walk in Lean would be no more trustworthy than the Python.
-/

namespace QOU.BraidKnot.LaurentWalk

open LaurentPolynomial

/-- A computable Laurent polynomial over `ℚ`: a list of `(exponent,
coefficient)` terms, understood as their sum. Duplicate exponents are
permitted — normalisation is a separate operation, and imposing it as an
invariant would have to be re-established after every step for no gain in the
semantics. -/
abbrev CLaurent : Type := List (ℤ × ℚ)

/-- What a `CLaurent` denotes: the Laurent polynomial `∑ cᵢ · q^{eᵢ}`. -/
noncomputable def denote : CLaurent → ℚ[T;T⁻¹]
  | [] => 0
  | (e, c) :: t => C c * T e + denote t

@[simp] theorem denote_nil : denote [] = 0 := rfl

@[simp] theorem denote_cons (e : ℤ) (c : ℚ) (t : CLaurent) :
    denote ((e, c) :: t) = C c * T e + denote t := rfl

/-! ## The computable operations -/

/-- Addition is concatenation: no term collection is required for the sum to
be correct. -/
def cadd (a b : CLaurent) : CLaurent := a ++ b

/-- Multiplication by `h = q - q⁻¹` is a shift-and-negate on each term — the
computable counterpart of `hQ_mul_T`, and the reason the walk is linear in the
number of terms rather than quadratic. -/
def cmulH (a : CLaurent) : CLaurent :=
  a.flatMap fun p => [(p.1 + 1, p.2), (p.1 - 1, -p.2)]

/-- Scaling by a rational coefficient. -/
def csmul (c : ℚ) (a : CLaurent) : CLaurent := a.map fun p => (p.1, c * p.2)

/-- The unit: `q⁰`. -/
def cone : CLaurent := [(0, 1)]

/-! ## Bridge lemmas — each computable operation denotes the abstract one -/

/-- Concatenation denotes the sum. Stated for `++` directly so it can be
used to reason about `List.flatMap`, which produces appends. -/
theorem denote_append (a b : CLaurent) :
    denote (a ++ b) = denote a + denote b := by
  induction a with
  | nil => simp
  | cons p t ih =>
      obtain ⟨e, c⟩ := p
      simp only [List.cons_append, denote_cons, ih]
      rw [add_assoc]

@[simp] theorem denote_cadd (a b : CLaurent) :
    denote (cadd a b) = denote a + denote b := denote_append a b

@[simp] theorem denote_csmul (c : ℚ) (a : CLaurent) :
    denote (csmul c a) = C c * denote a := by
  induction a with
  | nil => simp [csmul]
  | cons p t ih =>
      obtain ⟨e, d⟩ := p
      simp only [csmul, List.map_cons, denote_cons] at ih ⊢
      rw [ih, mul_add, ← mul_assoc, ← map_mul]

/-- **The load-bearing bridge lemma.** The computable shift-and-negate on
exponents denotes multiplication by `h = q - q⁻¹`. This is what makes the
executable walk a computation *of the abstract object* rather than a second,
unverified program that happens to be written in Lean. -/
@[simp] theorem denote_cmulH (a : CLaurent) :
    denote (cmulH a) = hQ * denote a := by
  induction a with
  | nil => simp [cmulH]
  | cons p t ih =>
      obtain ⟨e, c⟩ := p
      have hstep : cmulH ((e, c) :: t) = [(e + 1, c), (e - 1, -c)] ++ cmulH t := rfl
      rw [hstep, denote_append, ih, denote_cons, denote_cons, denote_nil,
          denote_cons, mul_add]
      congr 1
      rw [map_neg, mul_left_comm, hQ_mul_T, mul_sub]
      ring

@[simp] theorem denote_cone : denote cone = 1 := by
  simp [cone, T_zero]

/-! ## The six-component normal form and its step

`dim H₃ = 3! = 6`, so the Gröbner–Shirshov normal form is a six-vector of
Laurent coefficients — for *any* nucleus, at any nucleon number. The tables
below are transcribed from `hecke_core_symbolic.hm_sym`, which the module
docstring there records as mirroring `pyhecke.gram.hm` line for line. -/

/-- A normal-form state: six Laurent coefficients over the GS basis of `H₃`. -/
abbrev NF6 : Type := Fin 6 → CLaurent

/-- Which multiplier a table entry carries: the identity `c = 1`, the product
`c·h`, or the step's own coefficient `d`. -/
inductive Mult where
  | c    : Mult   -- multiplier 1
  | ch   : Mult   -- multiplier h
  | d    : Mult   -- multiplier d = dRat · h^(if dH then 1 else 0)
  deriving DecidableEq, Repr

/-- Transfer table for generator `σ₀`, as `(source, target, multiplier)`. -/
def table0 : List (Fin 6 × Fin 6 × Mult) :=
  [(0, 1, .c), (0, 0, .d),
   (1, 1, .ch), (1, 0, .c), (1, 1, .d),
   (2, 3, .c), (2, 2, .d),
   (3, 3, .ch), (3, 2, .c), (3, 3, .d),
   (4, 5, .c), (4, 4, .d),
   (5, 5, .ch), (5, 4, .c), (5, 5, .d)]

/-- Transfer table for generator `σ₁`. -/
def table1 : List (Fin 6 × Fin 6 × Mult) :=
  [(0, 2, .c), (0, 0, .d),
   (1, 4, .c), (1, 1, .d),
   (2, 2, .ch), (2, 0, .c), (2, 2, .d),
   (3, 5, .c), (3, 3, .d),
   (4, 4, .ch), (4, 1, .c), (4, 4, .d),
   (5, 5, .ch), (5, 3, .c), (5, 5, .d)]

/-- The contribution a single table entry makes, before it is accumulated. -/
def contrib (dRat : ℚ) (dH : Bool) : Mult → CLaurent → CLaurent
  | .c,  p => p
  | .ch, p => cmulH p
  | .d,  p => if dRat = 0 then [] else csmul dRat (if dH then cmulH p else p)

/-- One normal-form step: `nf ← nf · (σ_gen + d)` with `d = dRat · h^dH`.
Every multiplier used is `1`, `h`, or a rational times one of them — which is
precisely the hypothesis shape of `walk_mem_spanRange`. -/
def hmStep (dRat : ℚ) (dH : Bool) (gen : Bool) (nf : NF6) : NF6 := fun t =>
  ((if gen then table1 else table0).foldl
    (fun acc e => if e.2.1 = t then cadd acc (contrib dRat dH e.2.2 (nf e.1)) else acc)
    ([] : CLaurent))

/-- The identity normal form, `q⁰` in the first basis slot. -/
def nfOne : NF6 := fun i => if i = 0 then cone else []

/-! ## The atom braid word

Transcribed from `hecke_core_symbolic.build_atom_nf_sym`. The per-nucleon
chain, the `O(A²)` inter-nucleon loop and the trailing electron chain are all
present; the multipliers are exactly `1`, `0`, `-h` and `-h/2`, which is the
fact the Python probe relies on and which `walk_mem_spanRange` takes as its
hypothesis rather than assuming. -/

/-- Interleaved proton/neutron ordering, mirroring `_ground_state_ordering`.
`true` is a proton. -/
def ordering (Z N : ℕ) : List Bool :=
  let rec go : ℕ → ℕ → ℕ → List Bool
    | 0, _, _ => []
    | k + 1, pc, nc =>
        let isP := (((Z + N) - (k + 1)) % 2 = 0 && pc < Z) || nc ≥ N
        isP :: go k (if isP then pc + 1 else pc) (if isP then nc else nc + 1)
  go (Z + N) 0 0

/-- The step list for one nucleon: `(dRat, dH, gen)` triples. -/
def nucleonSteps (isProton : Bool) : List (ℚ × Bool × Bool) :=
  let three : List (ℚ × Bool × Bool) :=
    [(0, false, false), (-1, true, true),
     (0, false, false), (-1, true, true),
     (0, false, false), (-1, true, true)]
  if isProton then
    three ++ [(0, false, false), (-1/2, true, false), (-1/2, true, true),
              (0, false, false), (0, false, false)]
  else
    three ++ [(-1/2, true, false), (-1/2, true, false), (-1, true, true),
              (0, false, false), (0, false, false)]

/-- The interface step between two nucleons. -/
def interfaceStep (ti tj : Bool) : ℚ × Bool × Bool :=
  if ti && tj then (0, false, false)
  else if !ti && !tj then (-1, true, false)
  else (-1/2, true, false)

/-- Run a list of steps. -/
def runSteps (steps : List (ℚ × Bool × Bool)) (nf : NF6) : NF6 :=
  steps.foldl (fun s e => hmStep e.1 e.2.1 e.2.2 s) nf

/-- The full atom normal form, computed. -/
def atomNF (Z N : ℕ) : NF6 :=
  let ord := ordering Z N
  let stepsFor (k : ℕ) : List (ℚ × Bool × Bool) :=
    let tk := ord.getD k true
    nucleonSteps tk ++
      ((List.range k).map (fun prev => interfaceStep (ord.getD prev true) tk))
  let body := (List.range (Z + N)).flatMap stepsFor
  let electrons := (List.replicate Z ((-1 : ℚ), true, true))
  runSteps (body ++ electrons) nfOne

/-! ## Normalisation and the measured degrees

`denote` is insensitive to duplicate exponents, so the walk above needs no
normalisation to be *correct*. Reading a degree off it does require collecting
terms, because cancellation can shrink the true span.

**This is the remaining piece and it is not faked here.** `cnorm` below
collects terms, but the bridge lemma `denote_cnorm : denote (cnorm a) =
denote a` is NOT yet proved, so no degree computed through it is asserted as a
theorem anywhere in this file. Until that lemma lands, the exponents read off
the raw walk are *bounds* on the span, not the span — which is exactly what
`walk_mem_spanRange` already gives abstractly. The measured degrees stay in
the probe's witness and are not restated here as Lean claims. -/

/-- Collect duplicate exponents and drop zero coefficients. -/
def cnorm (a : CLaurent) : CLaurent :=
  let exps := (a.map Prod.fst).eraseDups
  (exps.map (fun e => (e, (a.filter (fun p => p.1 = e)).foldl (fun s p => s + p.2) 0))).filter
    (fun p => p.2 != 0)

/-- Raw term count of the walk, before collection: a computable upper bound on
the number of distinct monomials. -/
def rawTerms (Z N : ℕ) : ℕ :=
  ((List.finRange 6).map (fun i => (atomNF Z N i).length)).sum

end QOU.BraidKnot.LaurentWalk
