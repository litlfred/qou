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
agreeing, not a proof. `degreeProfile 1 0 = [some 10, …]` closed with `rfl`
FAILS.

**🛑 CORRECTION to my own first explanation of that failure.** I wrote here
that the cause was size: the unnormalised walk builds a 177,045-term
intermediate (`rawTerms 1 0`) before collection leaves 59. **That was a
hypothesis and it is refuted.** `denote_cnorm` is now proved, `atomNFN`
collects after every step so the kernel sees the true 11/12/10/9/11/6 terms,
and `rfl` fails exactly as before. Bisecting:

    (cmulH [(0, 1)]).length = 2                     rfl SUCCEEDS
    cnorm [((0:ℤ), (1:ℚ)), (0, -1)] = []            rfl FAILS  ← two terms
    (hmStep (-1) true false nfOne 0).length = 1     rfl FAILS

So the obstruction is **`Rat` decidable equality in the kernel**, not the term
count. `cinsert` tests `c + c' = 0` and `contrib` tests `dRat = 0`; `Rat`
carries a `Nat.gcd` normalisation invariant that the kernel will not reduce
through. A two-term list is already enough to hit it, and no amount of
collecting helps.

**The fix is principled, not a workaround.** The atom path's coefficients are
only `1`, `0`, `-1` and `-1/2`, so the walk lives in `ℤ[1/2][q^{±1}]`: carry
`ℤ` coefficients together with a single power-of-two scale, and every
comparison becomes `Int` equality, which the kernel does reduce. That is the
next step, and `denote_cnorm` above is what will license the re-scaling as
denotation-preserving.

`decide` is worse than `rfl` here and `native_decide` is banned outright by
the repo's Strict Lean Discipline, so neither is an escape.

**Still open, and not faked anywhere below:** no degree is asserted as a
theorem in this file. `degreeProfile` and `termProfile` are *computed*, and
`denote_cnorm` says the collection they run through preserves the denotation
— but the numbers themselves reach the reader through `#eval`, and are
reported as such.

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

/-- Insert a single term into a list, combining it with any existing term at
the same exponent and dropping the result when it cancels.

Defined by recursion rather than by grouping-and-summing, because each step is
then a small equation that `denote` can be pushed through — which is what
makes `denote_cinsert` provable at all. -/
def cinsert (e : ℤ) (c : ℚ) : CLaurent → CLaurent
  | [] => if c = 0 then [] else [(e, c)]
  | (e', c') :: t =>
      if e' = e then (if c + c' = 0 then t else (e, c + c') :: t)
      else (e', c') :: cinsert e c t

/-- **Insertion denotes adding the term.** The cancellation branch is the one
that matters: dropping a term whose coefficients sum to zero does not change
what the list denotes. -/
theorem denote_cinsert (e : ℤ) (c : ℚ) (a : CLaurent) :
    denote (cinsert e c a) = C c * T e + denote a := by
  induction a with
  | nil =>
      by_cases hc : c = 0
      · simp [cinsert, hc]
      · simp [cinsert, hc]
  | cons p t ih =>
      obtain ⟨e', c'⟩ := p
      by_cases he : e' = e
      · subst he
        have hun : cinsert e' c ((e', c') :: t)
            = (if c + c' = 0 then t else (e', c + c') :: t) := by
          simp [cinsert]
        rw [hun]
        by_cases hz : c + c' = 0
        · have hcc : C c * T e' + C c' * T e' = (0 : ℚ[T;T⁻¹]) := by
            rw [← add_mul, ← map_add, hz, map_zero, zero_mul]
          rw [if_pos hz]
          simp only [denote_cons]
          rw [← add_assoc, hcc, zero_add]
        · rw [if_neg hz]
          simp only [denote_cons]
          rw [← add_assoc, ← add_mul, ← map_add]
      · have hun : cinsert e c ((e', c') :: t) = (e', c') :: cinsert e c t := by
          simp [cinsert, he]
        rw [hun]
        simp only [denote_cons, ih]
        rw [← add_assoc, ← add_assoc, add_comm (C c' * T e')]

/-- Collect duplicate exponents and drop zero coefficients. -/
def cnorm : CLaurent → CLaurent
  | [] => []
  | (e, c) :: t => cinsert e c (cnorm t)

/-- **Normalisation preserves the denotation.**

This is what licenses reading a degree off `cnorm`: the collected list denotes
the same Laurent polynomial as the raw walk, so its exponents really are the
exponents of the polynomial the walk computes, not an artefact of collection. -/
@[simp] theorem denote_cnorm (a : CLaurent) : denote (cnorm a) = denote a := by
  induction a with
  | nil => rfl
  | cons p t ih =>
      obtain ⟨e, c⟩ := p
      rw [cnorm, denote_cinsert, ih, denote_cons]

/-! ## The normalising walk

`denote_cnorm` licenses collecting terms after every step rather than only at
the end. That is not a cosmetic change: the unnormalised walk builds a
177,045-term intermediate for a single proton, which is why the kernel cannot
check it; collecting each step keeps every coefficient at its true term count
(11, 12, 10, 9, 11, 6 for the proton) and brings the computation into range. -/

/-- One step, with the result collected. Denotes the same thing as `hmStep`
by `denote_cnorm`. -/
def hmStepN (dRat : ℚ) (dH : Bool) (gen : Bool) (nf : NF6) : NF6 :=
  fun t => cnorm (hmStep dRat dH gen nf t)

/-- Normalising a step changes nothing about what it denotes. -/
theorem denote_hmStepN (dRat : ℚ) (dH gen : Bool) (nf : NF6) (t : Fin 6) :
    denote (hmStepN dRat dH gen nf t) = denote (hmStep dRat dH gen nf t) :=
  denote_cnorm _

/-- Run a list of steps, collecting after each. -/
def runStepsN (steps : List (ℚ × Bool × Bool)) (nf : NF6) : NF6 :=
  steps.foldl (fun s e => hmStepN e.1 e.2.1 e.2.2 s) nf

/-- The atom normal form, collected at every step. -/
def atomNFN (Z N : ℕ) : NF6 :=
  let ord := ordering Z N
  let stepsFor (k : ℕ) : List (ℚ × Bool × Bool) :=
    let tk := ord.getD k true
    nucleonSteps tk ++
      ((List.range k).map (fun prev => interfaceStep (ord.getD prev true) tk))
  let body := (List.range (Z + N)).flatMap stepsFor
  let electrons := (List.replicate Z ((-1 : ℚ), true, true))
  runStepsN (body ++ electrons) nfOne

/-- The q-degree profile: the maximum exponent of each of the six
coefficients. Because the walk is collected at every step and
`denote_cnorm` says collection preserves the denotation, these are the
exponents of the polynomials the walk computes. -/
def degreeProfile (Z N : ℕ) : List (Option ℤ) :=
  (List.finRange 6).map (fun i => ((atomNFN Z N i).map Prod.fst).max?)

/-- Term count per coefficient. -/
def termProfile (Z N : ℕ) : List ℕ :=
  (List.finRange 6).map (fun i => (atomNFN Z N i).length)

/-- Raw term count of the walk, before collection: a computable upper bound on
the number of distinct monomials. -/
def rawTerms (Z N : ℕ) : ℕ :=
  ((List.finRange 6).map (fun i => (atomNF Z N i).length)).sum

end QOU.BraidKnot.LaurentWalk
