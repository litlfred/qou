import Mathlib.Tactic

/-!
# QOU.Eightfold.GellMannOkuboSecondOrder — what a second-order term can and cannot carry

Bean `qou-bhfg`. Sequel to `QOU.Eightfold.GellMannOkuboIdentity`, which proves
Gell-Mann–Okubo vanishes **identically** in the first-order octet ansatz and so
has zero discriminating power.

## The question this answers

If GMO is content-free at first order, the testable content is its **deviation**
(≈ 6 %), and likewise the decuplet equal-spacing deviation (≈ 9.2 %). The
framework derives no second-order term, so it currently predicts **0** for both.
Before anyone fits a term to those numbers, it is worth knowing *which*
second-order structures can carry them at all — a formalize-first prune
(AGENTS.md §"Formalize-first probe discipline").

## The ansatz

First order is `m = a + b·Y + c·d` with `d = I(I+1) − Y²/4`. At second order the
three structures quadratic in the breaking are `Y²`, `d²` and `Y·d`, with
coefficients `e`, `f`, `g`. Everything is scaled by 16 and written through
`fourD = 4·I(I+1) − Y²` so that no denominator ever appears; the scaling is
uniform and cancels from every statement below.

## What is proved

| declaration | content |
|---|---|
| `gmo_second_order` | the GMO combination is `16·(4e − 3f)` |
| `gmo_blind_to_Yd` | **GMO cannot see `g` at all** — the `Y·d` structure is odd in `Y` and dies in the hypercharge-averaged kaon |
| `decuplet_second_differences_equal` | the two decuplet second differences stay **exactly equal** |
| `decuplet_second_order` | each is `8·(4e + 9f + 6g)` |
| `gmo_zero_decuplet_nonzero` / `decuplet_zero_gmo_nonzero` | the two constraints are **independent** — witnesses both ways |
| `meson_octet_g_absorbed` / `decuplet_g_absorbed` | **`g` is not an independent parameter on either multiplet** — absorbed exactly by shifting `b` (and `e`) |
| `meson_octet_second_order_surjective` | **any three meson-octet masses are attainable**, so second-order GMO is vacuous |
| `baryon_octet_second_order_surjective` | **any four baryon-octet masses are attainable** — the baryon case is vacuous too |

## What it means, stated carefully

Two consequences, and neither is a derivation of anything:

1. **`Y·d` is invisible to GMO.** Not "small" — *exactly* zero, by parity in `Y`.
   A GMO-deviation fit therefore cannot constrain `g` even in principle.
2. **The octet has nothing left to predict.** GMO constrains `4e − 3f`; the
   decuplet constrains `4e + 9f + 6g`; those are not proportional, so the two
   deviations are independent. My first reading of that was *"two equations,
   three unknowns — find a third constraint on the coefficients."* **That was
   wrong**, and the `Absorption` and `Surjectivity` sections below say why.
   `g` is not a free direction on either multiplet: it is absorbed exactly by
   shifting `b` (octet) or `b` and `e` (decuplet), because in each multiplet the
   isospin is a function of the hypercharge. So the residual freedom is a
   reparametrisation, and no categorical argument forcing `g = 0` would buy
   anything — it would be a statement about a coordinate.

   The real obstruction is stronger and sits one level up: at second order the
   even-in-`Y` structures already span **all** functions on the three
   independent meson-octet masses. Any `(m_π, m_η, m_K)` whatsoever is
   attainable, so the GMO combination takes every value and there is no relation
   left to deviate from. Matching the observed deviation is not a weak
   prediction — it is not a prediction at all. The same holds for the **baryon**
   octet (`BaryonOctet` section below), which I first got backwards; the decuplet
   is the only one of the three that keeps a relation. What is needed is not
   another multiplet from this list but a **derivation** of `e`, `f`, `g` — see
   the closing section.

The equal-spacing result is worth stating precisely, because it is easy to
over-read. At second order the decuplet is **not** equally spaced — each second
difference is `8·(4e + 9f + 6g) ≠ 0` in general. What survives is that the two
second differences remain *equal to each other*: the failure is uniform, so the
decuplet masses go from linear to exactly quadratic in the ladder position, with
no cubic residue. That is a real constraint on any second-order account, and it
is testable against the observed spacings independently of their common size.

**Scope.** This is a statement about the standard `(I, Y)` octet/decuplet mass
ansatz, consumed as given — the same ansatz `GellMannOkuboIdentity` uses. It
derives no value for `e`, `f`, `g`, predicts neither deviation, and says nothing
about whether QOU produces such a term. Coleman–Glashow is deliberately **not**
included: it is an electromagnetic/isospin-breaking relation, not an
`SU(3)`-breaking one on this ansatz, and folding it in here would be the
overloaded-symbol error this branch has already had to correct once.

-- Ref: [okubo1962] (the octet mass formula and its `SU(3)`-breaking expansion).
-/

namespace QOU.Eightfold.GellMannOkuboSecondOrder

variable {R : Type*} [CommRing R]

/-- `16 ×` the mass of a state, with first-order coefficients `a, b, c` and
second-order `e` (`Y²`), `f` (`d²`), `g` (`Y·d`).

`fourD = 4·I(I+1) − Y²`, i.e. `4d`. The `16 ×` and the `fourD` parametrisation
between them clear every denominator; both scalings are uniform across states
and cancel from every combination below. -/
def m16 (a b c e f g : R) (fourD Y : R) : R :=
  16 * a + 16 * b * Y + 4 * c * fourD + 16 * e * Y ^ 2 + f * fourD ^ 2 + 4 * g * Y * fourD

section Meson
variable (a b c e f g : R)

/-- Pion: `I = 1, Y = 0` ⇒ `fourD = 8`. -/
def pion : R := m16 a b c e f g 8 0
/-- Eta: `I = 0, Y = 0` ⇒ `fourD = 0`. -/
def eta : R := m16 a b c e f g 0 0
/-- Kaon at `Y = +1`: `I = 1/2` ⇒ `fourD = 2`. -/
def kaonPlus : R := m16 a b c e f g 2 1
/-- Kaon at `Y = −1`. -/
def kaonMinus : R := m16 a b c e f g 2 (-1)

/-- The GMO combination `4·⟨m²_K⟩ − 3·m²_η − m²_π`, doubled so the hypercharge
average over the kaon doublet needs no division. -/
def gmoCombination : R := 2 * (kaonPlus a b c e f g + kaonMinus a b c e f g)
  - 3 * eta a b c e f g - pion a b c e f g

/-- **GMO at second order is `16·(4e − 3f)`.** It vanishes identically in the
first-order parameters `a, b, c` — recovering `GellMannOkuboIdentity` — and
picks up exactly one combination of the second-order ones. -/
theorem gmo_second_order : gmoCombination a b c e f g = 16 * (4 * e - 3 * f) := by
  unfold gmoCombination kaonPlus kaonMinus eta pion m16; ring

/-- **GMO is blind to the `Y·d` structure.** Changing `g` freely leaves the
combination unchanged — it is odd in `Y` and cancels in the kaon average. So a
fit to the GMO deviation cannot constrain `g`, even in principle. -/
theorem gmo_blind_to_Yd (g' : R) :
    gmoCombination a b c e f g = gmoCombination a b c e f g' := by
  rw [gmo_second_order, gmo_second_order]

end Meson

section Decuplet
variable (a b c e f g : R)

/-- Δ: `I = 3/2, Y = 1` ⇒ `fourD = 14`. -/
def delta : R := m16 a b c e f g 14 1
/-- Σ*: `I = 1, Y = 0` ⇒ `fourD = 8`. -/
def sigmaStar : R := m16 a b c e f g 8 0
/-- Ξ*: `I = 1/2, Y = −1` ⇒ `fourD = 2`. -/
def xiStar : R := m16 a b c e f g 2 (-1)
/-- Ω: `I = 0, Y = −2` ⇒ `fourD = −4`. -/
def omega : R := m16 a b c e f g (-4) (-2)

/-- Upper second difference `Ω − 2Ξ* + Σ*`; zero iff the top three are equally
spaced. -/
def spacingUpper : R := omega a b c e f g - 2 * xiStar a b c e f g + sigmaStar a b c e f g
/-- Lower second difference `Ξ* − 2Σ* + Δ`. -/
def spacingLower : R := xiStar a b c e f g - 2 * sigmaStar a b c e f g + delta a b c e f g

/-- **The equal-spacing rule fails at second order** — each second difference is
`8·(4e + 9f + 6g)`, nonzero in general. -/
theorem decuplet_second_order :
    spacingUpper a b c e f g = 8 * (4 * e + 9 * f + 6 * g) := by
  unfold spacingUpper omega xiStar sigmaStar m16; ring

/-- **But the failure is uniform.** The two second differences remain *exactly*
equal, so the decuplet goes from linear to exactly quadratic in the ladder
position with no cubic residue — a constraint testable independently of the
common size of the deviation. -/
theorem decuplet_second_differences_equal :
    spacingUpper a b c e f g = spacingLower a b c e f g := by
  unfold spacingUpper spacingLower omega xiStar sigmaStar delta m16; ring

end Decuplet

/-! ## Independence — two measurements cannot fix three coefficients -/

/-- A second-order term with **zero** GMO deviation and a **nonzero** decuplet
one. -/
theorem gmo_zero_decuplet_nonzero :
    gmoCombination (0:ℤ) 0 0 3 4 0 = 0 ∧ spacingUpper (0:ℤ) 0 0 3 4 0 ≠ 0 := by
  constructor
  · rw [gmo_second_order]; decide
  · rw [decuplet_second_order]; decide

/-- And one with a **nonzero** GMO deviation and **zero** decuplet one. So the
two relations constrain genuinely different combinations.

The leftover freedom is **not** a missing physical constraint — see
`meson_octet_g_absorbed` and `decuplet_g_absorbed` below, which show `g` is
absorbed exactly by the lower-order coefficients on both multiplets. -/
theorem decuplet_zero_gmo_nonzero :
    spacingUpper (0:ℤ) 0 0 3 (-4) 4 = 0 ∧ gmoCombination (0:ℤ) 0 0 3 (-4) 4 ≠ 0 := by
  constructor
  · rw [decuplet_second_order]; decide
  · rw [gmo_second_order]; decide

/-! ## The `Y·d` structure is not an independent parameter — on either multiplet

The independence witnesses above show GMO and the decuplet constrain different
combinations, and I first read that as *"two equations, three unknowns, so a
third constraint on the coefficients would close it."* **That reading is wrong,
and the two theorems in this section are why.**

`g` is not a free direction on the octet or on the decuplet. It is absorbed
exactly — no residue, not merely to leading order — by shifting the *lower*-order
coefficients, because in each multiplet the isospin is pinned by the hypercharge:

* **Octet.** Hypercharge `±1` forces `I = 1/2`, hence `fourD = 2`; and the two
  `Y = 0` states kill the `g` term outright. So `Y·fourD = 2Y` on every octet
  state, and `g` is a disguised `b`.
* **Decuplet.** `I = 1 + Y/2` along the whole ladder, hence
  `fourD = 8 + 6Y` identically; so `Y·fourD = 8Y + 6Y²`, and `g` is a disguised
  mixture of `b` and `e`.

So looking for a categorical argument that forces `g = 0` would be proving
something about a *coordinate*, not about the physics: `g` can be set to zero by
reparametrisation, on both multiplets, losing nothing. -/

section Absorption
variable {R : Type*} [Field R] [CharZero R]
variable (a b c e f g : R)

/-- **On the octet, `g` is a disguised `b`.** Shifting `b ↦ b + g/2` reproduces
every meson-octet mass with `g = 0`. Exact, all four states. -/
theorem meson_octet_g_absorbed :
    pion a b c e f g = pion a (b + g / 2) c e f 0
      ∧ eta a b c e f g = eta a (b + g / 2) c e f 0
      ∧ kaonPlus a b c e f g = kaonPlus a (b + g / 2) c e f 0
      ∧ kaonMinus a b c e f g = kaonMinus a (b + g / 2) c e f 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [pion, eta, kaonPlus, kaonMinus, m16] <;> ring

/-- **On the decuplet, `g` is a disguised `b` and `e`.** Shifting
`b ↦ b + 2g` and `e ↦ e + 3g/2` reproduces every decuplet mass with `g = 0`.
The shift in `e` is exactly the `6g` visible in `decuplet_second_order`. -/
theorem decuplet_g_absorbed :
    delta a b c e f g = delta a (b + 2 * g) c (e + 3 * g / 2) f 0
      ∧ sigmaStar a b c e f g = sigmaStar a (b + 2 * g) c (e + 3 * g / 2) f 0
      ∧ xiStar a b c e f g = xiStar a (b + 2 * g) c (e + 3 * g / 2) f 0
      ∧ omega a b c e f g = omega a (b + 2 * g) c (e + 3 * g / 2) f 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [delta, sigmaStar, xiStar, omega, m16] <;> ring

end Absorption

/-! ## At second order the meson octet is *unconstrained* — GMO has nothing left

The sharper statement, and the one that prunes the search. It is not that the
second-order ansatz predicts the GMO deviation badly, or predicts it only up to a
free parameter. It is that **the ansatz can produce any three meson-octet masses
whatsoever**, so there is no relation among them left to deviate from.

Three physical masses are available — `π`, `η`, and the charge-conjugation-
degenerate kaon — and the even-in-`Y` structures `1`, `Y²`, `fourD²` already
span all functions on those three states. The witness below sets `b = c = g = 0`,
so it does not even need the odd sector.

**Consequence, stated as a scope-(b) exclusion with its invariant named** (the
invariant is the rank count: three independent structures on three independent
masses): *no* second-order term in `(I, Y)` on this ansatz can carry predictive
content about the meson octet. Fitting one to the observed deviation is
therefore not a weak prediction — it is not a prediction at all. This is a
statement about **this ansatz**, not about `SU(3)` breaking in general. -/

section Surjectivity
variable {R : Type*} [Field R] [CharZero R]

/-- **Any three meson-octet masses are attainable at second order.** Given
targets `p, h, k` for pion, eta and kaon, explicit coefficients reproduce all
three — and the kaon doublet stays degenerate, since the witness has `b = g = 0`.

Hence the Gell-Mann–Okubo relation, which is an identity at first order
(`GellMannOkuboIdentity`), is **vacuous** at second order: its combination can
take any value at all, so matching the observed ≈ 6 % deviation constrains
nothing. -/
theorem meson_octet_second_order_surjective (p h k : R) :
    ∃ a e f : R,
      pion a 0 0 e f 0 = p
        ∧ eta a 0 0 e f 0 = h
        ∧ kaonPlus a 0 0 e f 0 = k
        ∧ kaonMinus a 0 0 e f 0 = k := by
  refine ⟨h / 16, (k - h) / 16 - (p - h) / 256, (p - h) / 64, ?_, ?_, ?_, ?_⟩ <;>
    simp only [pion, eta, kaonPlus, kaonMinus, m16] <;> ring

/-- **The GMO combination takes every value.** Immediate from surjectivity, and
worth stating on its own: there is no value of the deviation that would count as
evidence for or against a second-order term. -/
theorem gmo_combination_surjective (t : R) :
    ∃ a b c e f g : R, gmoCombination a b c e f g = t := by
  refine ⟨0, 0, 0, t / 64, 0, 0, ?_⟩
  rw [gmo_second_order]; ring

end Surjectivity

/-! ## What survives on the decuplet, and what would actually close this

The decuplet is **not** surjective in the same way, and that asymmetry is the
one piece of testable content left. Because `fourD = 8 + 6Y` along the ladder,
every structure in the ansatz — `Y`, `d`, `Y²`, `d²`, `Y·d` alike — restricts to
a polynomial in `Y` alone, of degree at most two. Four states, a three-
dimensional space of quadratics: exactly one relation survives, and it is
`decuplet_second_differences_equal` above.

That also bounds what refining the *structure list* can buy: adding cubic
structures would raise the degree to three and destroy the last relation rather
than create a new one.

I originally continued this paragraph with *"what is needed is a third multiplet
in which isospin is not a function of hypercharge — the baryon octet is such a
multiplet."* **That was wrong**; the `BaryonOctet` section below retracts it and
proves the baryon octet surjective as well. The corrected prescription is there,
and it is a derivation of the coefficients rather than another multiplet. -/

/-! ## The baryon octet — and the correction it forces

I claimed, in the section above and in the PR that carried it, that the baryon
octet is the multiplet where the relation survives, *"which is why baryon GMO is
a genuine relation where the meson one has become vacuous."* **That is wrong,
and this section is the retraction.**

The reasoning I gave was that `Λ` and `Σ` share `Y = 0` with different `I`, so
`d` is not a function of `Y` on the baryon octet. The premise is true. The
inference is backwards: a two-dimensional `(I, Y)` pattern makes the space of
available structures **larger**, and a larger structure space makes surjectivity
*more* likely, not less. Rank counting settles it —

| multiplet | independent masses | rank of the second-order structure space | relations |
|---|---|---|---|
| meson octet | 3 (`K⁺ = K⁻` by charge conjugation) | 3 | **0** |
| baryon octet | 4 | 4 | **0** |
| decuplet | 4 | 3 (`I = 1 + Y/2` ⇒ everything is a quadratic in `Y`) | **1** |

So **both** octets go vacuous at second order and the decuplet's equal-second-
differences rule is the only `SU(3)` mass relation among the three that survives.
The general criterion is the last column: a multiplet retains a relation exactly
when its number of independent masses exceeds the rank of the structure space on
it, and the octets fail that test because their `(I, Y)` patterns are generic,
not because they are degenerate.

**What this does to "what would close it."** Not a third multiplet from this
list — that was the wrong prescription and it followed from the wrong premise.
Two routes remain, and the second is the framework-native one:

1. A multiplet with **more independent masses than the six available structures**
   — anything beyond six distinct `(I, Y)` values retains relations at second
   order regardless of its pattern. Nothing in this corpus supplies one.
2. **Deriving `e`, `f`, `g`** from the categorical side rather than measuring
   them. The rank counting says measurement can *never* make the octet masses
   predictions, at any order: a structure space that spans everything absorbs any
   spectrum. Only theory input can. That is the honest reading of what front 4
   established. -/

section BaryonOctet
variable {R : Type*} [CommRing R]
variable (a b c e f g : R)

/-- Nucleon: `I = 1/2, Y = 1` ⇒ `fourD = 2`. -/
def nucleon : R := m16 a b c e f g 2 1
/-- `Λ`: `I = 0, Y = 0` ⇒ `fourD = 0`. -/
def lambdaB : R := m16 a b c e f g 0 0
/-- `Σ`: `I = 1, Y = 0` ⇒ `fourD = 8`. -/
def sigmaB : R := m16 a b c e f g 8 0
/-- `Ξ`: `I = 1/2, Y = −1` ⇒ `fourD = 2`. -/
def xiB : R := m16 a b c e f g 2 (-1)

/-- The baryon GMO combination `2(m_N + m_Ξ) − 3m_Λ − m_Σ`, i.e. the doubled form
of `(m_N + m_Ξ)/2 = (3m_Λ + m_Σ)/4`. -/
def gmoBaryon : R :=
  2 * (nucleon a b c e f g + xiB a b c e f g) - 3 * lambdaB a b c e f g - sigmaB a b c e f g

/-- **The baryon combination has the same second-order value as the meson one**,
`16(4e − 3f)` — `g` cancels here too. The two octets carry the same `(I, Y)`
pattern (`π ↔ Σ`, `η ↔ Λ`, `K⁺ ↔ N`, `K⁻ ↔ Ξ`), so this is not a coincidence. -/
theorem gmo_baryon_second_order : gmoBaryon a b c e f g = 16 * (4 * e - 3 * f) := by
  unfold gmoBaryon nucleon xiB lambdaB sigmaB m16; ring

/-- **On the baryon octet too, `g` is a disguised `b`** — the same `Y·fourD = 2Y`
collapse, since hypercharge `±1` forces `I = 1/2` in either octet. -/
theorem baryon_octet_g_absorbed {R : Type*} [Field R] [CharZero R] (a b c e f g : R) :
    nucleon a b c e f g = nucleon a (b + g / 2) c e f 0
      ∧ lambdaB a b c e f g = lambdaB a (b + g / 2) c e f 0
      ∧ sigmaB a b c e f g = sigmaB a (b + g / 2) c e f 0
      ∧ xiB a b c e f g = xiB a (b + g / 2) c e f 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [nucleon, lambdaB, sigmaB, xiB, m16] <;> ring

/-- **Any four baryon-octet masses are attainable at second order.** This is the
retraction made precise: the baryon octet is surjective just as the meson octet
is, so baryon GMO is *also* vacuous at second order.

Note the witness needs `b ≠ 0` where the meson one did not — the baryon octet
has four independent masses rather than three, because `N` and `Ξ` are not
charge-conjugate partners. That extra mass is exactly matched by the extra
structure, which is why the rank still saturates. -/
theorem baryon_octet_second_order_surjective {R : Type*} [Field R] [CharZero R]
    (n l s x : R) :
    ∃ a b e f : R,
      nucleon a b 0 e f 0 = n
        ∧ lambdaB a b 0 e f 0 = l
        ∧ sigmaB a b 0 e f 0 = s
        ∧ xiB a b 0 e f 0 = x := by
  refine ⟨l / 16, (n - x) / 32, (n + x) / 32 - l / 16 - (s - l) / 256,
    (s - l) / 64, ?_, ?_, ?_, ?_⟩ <;>
    simp only [nucleon, lambdaB, sigmaB, xiB, m16] <;> ring

/-- **So the baryon GMO combination also takes every value.** Immediate from
surjectivity; stated because it is the claim the retraction is about. -/
theorem gmo_baryon_surjective {R : Type*} [Field R] [CharZero R] (t : R) :
    ∃ a b c e f g : R, gmoBaryon a b c e f g = t := by
  refine ⟨0, 0, 0, t / 64, 0, 0, ?_⟩
  rw [gmo_baryon_second_order]; ring

end BaryonOctet

end QOU.Eightfold.GellMannOkuboSecondOrder
