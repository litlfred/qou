/-
# Kernel-level borrowed-name / definitional-collapse audit

The regex sibling (`scripts/lean-borrowed-name-audit.py`) reads source text.
This reads the **environment**: for every declaration of a target module it asks
the elaborator, not a pattern, three questions.

1. `typeForeign`  — which constants occurring in the STATEMENT come from a
   different QOU/UGB module.  Empty means the statement is about nothing but
   this file's own definitions.  Computed from `Expr.getUsedConstants` on the
   type, resolved through `Environment.getModuleFor?` — exact, not a name guess.
2. `valueForeign` — the same for the PROOF TERM.  Empty means the proof imports
   no content from outside the file, whatever tactics spelled it.  This is
   spelling-independent by construction: `rw [foo]; rfl`, `simp [foo]` and
   `exact foo` all leave `foo` in the term.
3. `defeqCollapse` — does the statement's LHS reduce to its RHS at default
   transparency?  If yes the theorem is TRUE BY UNFOLDING ITS OWN DEFINITIONS
   and the proof is decoration, however elaborate it looks.

(3) is the check bean `qou-wcff` asked for and the one a text scanner cannot
approximate: definitional equality is decided by the kernel, not by the shape
of the tactic block.  Guarded by `maxHeartbeats` so a genuinely hard goal
returns `false` rather than hanging.
-/
import Lean
open Lean Meta Elab Command

namespace BorrowedNameKernel

/-- Corpus modules, as opposed to Mathlib/core. -/
def isCorpus (m : Name) : Bool :=
  (`QOU).isPrefixOf m || (`UGB).isPrefixOf m || (`Fred2005).isPrefixOf m

/-- Module a declaration was compiled in (`none` for the current module). -/
def modOf (env : Environment) (c : Name) : Option Name := do
  let idx ← env.getModuleIdxFor? c
  env.header.moduleNames[idx.toNat]?

/-- Constants used by `e` that live in a corpus module other than `self`. -/
def foreignCorpusConsts (env : Environment) (self : Name) (e : Expr) : Array Name :=
  e.getUsedConstants.filter fun c =>
    match modOf env c with
    | some m => isCorpus m && m != self
    | none   => false

/-- Constants used by `e` that are declared in `self`. -/
def localConsts (env : Environment) (self : Name) (e : Expr) : Array Name :=
  e.getUsedConstants.filter fun c => modOf env c == some self

/-- `Eq` application, destructured without depending on a recognizer's location. -/
def eqParts? : Expr → Option (Expr × Expr)
  | .app (.app (.app (.const ``Eq _) _) lhs) rhs => some (lhs, rhs)
  | _ => none

/-- Is the statement an equation whose sides are definitionally equal?
    Telescopes binders first, so `forall N d, f N d = g N d` is handled.
    THIS is the check a text scanner cannot approximate: definitional equality
    is decided by the kernel, not by the shape of the tactic block. -/
def defeqCollapse (type : Expr) : MetaM Bool := do
  try
    forallTelescopeReducing type fun _ body =>
      match eqParts? body with
      | some (lhs, rhs) => withDefault <| isDefEq lhs rhs
      | none            => pure false
  catch _ => pure false

/-- Is `c` a field projection of a structure/class -- `C.field`, the function
    Lean generates for reading one field out of an instance?

    Asked by NAME rather than through `getProjectionFnInfo?`, because the latter
    is a `CoreM` query and this predicate runs inside the per-constant loop where
    only `Environment` is to hand.  `isStructure` + `getStructureFields` is the
    same information: `C.f` is a projection exactly when `C` is a structure and
    `f` is one of its fields. -/
def isFieldProjection (env : Environment) (c : Name) : Bool :=
  match c with
  | .str parent field =>
      isStructure env parent && (getStructureFields env parent).contains (.mkSimple field)
  | _ => false

/-- Does the proof READ ITS CONCLUSION OUT OF ITS OWN HYPOTHESES and derive
    nothing else from this file?

    True when every constant the proof term uses **from this module** is a field
    projection.  The proof may still call foreign packaging (`And.intro`,
    `Iff.intro`, `Exists.intro`) and Mathlib lemmas -- what it may not do is
    invoke another declaration of its own file, because that would be a
    derivation step rather than a field read.

    This is the check batch 8 established the kernel pass was MISSING.
    `defeqCollapse` asks about the STATEMENT; the self-assuming projection
    (AGENTS.md 3b-cond rule 5) leaves the statement opaque -- `s.total` versus
    `s.smooth + s.oscillating` are two class-field applications and nothing
    reduces -- and puts the whole defect in the VALUE.  Measured 2026-08-30: over
    ten modules selected for exactly that family, `defeqCollapse` fired on 0 of
    the 5 it could see, in 117 theorems.

    Like `defeqCollapse`, a CANDIDATE signal and not a verdict.  A conditional
    theorem that legitimately discharges its goal from a stated hypothesis looks
    identical from here; what separates the two is whether the class carries the
    conclusion or its inputs, and that is a reading, not a computation.  The
    non-emptiness guard keeps out proofs that touch no local constant at all
    (`by norm_num`, a pure Mathlib citation), which are a different question.

    TRAP, measured 2026-08-30 and worth stating because the first version of this
    predicate reported ZERO on five modules chosen for containing the defect.
    Field access on an instance leaves BOTH the projection AND THE STRUCTURE
    ITSELF in `getUsedConstants`: `s.split_identity` yields
    `[CommRing, GradedTraceResidueSplit, GradedTraceResidueSplit.split_identity]`.
    So `ls.all isFieldProjection` is always false whenever the structure is local,
    which is exactly the case this is for.  The structure name must be admitted
    alongside its fields, and the non-emptiness guard moved onto the PROJECTIONS
    so that merely mentioning a local structure type is not enough to fire. -/
def valueOnlyProjects (env : Environment) (self : Name) (v : Expr) : Bool :=
  let ls := localConsts env self v
  let projs := ls.filter (isFieldProjection env)
  !projs.isEmpty && ls.all fun c => isFieldProjection env c || isStructure env c

/-- Is the proof term a reflexivity proof, after stripping lambdas? -/
partial def valueIsRfl : Expr -> Bool
  | .lam _ _ b _  => valueIsRfl b
  | .mdata _ b    => valueIsRfl b
  | e             => match e.getAppFn with
                     | .const n _ => n == ``Eq.refl || n == ``rfl
                     | _          => false

/-- Equation lemmas, match auxiliaries and proof obligations the compiler
    emits.  These are definitional by construction and are not authored claims. -/
def isAutoGenerated : Name -> Bool
  | .str p sfx =>
      sfx == "eq_def" || sfx == "sizeOf_spec" || sfx == "injEq" || sfx == "noConfusion"
      || (sfx.startsWith "eq_"    && (sfx.drop 3).all Char.isDigit && sfx.length > 3)
      || (sfx.startsWith "match_" && (sfx.drop 6).all Char.isDigit)
      || (sfx.startsWith "proof_" && (sfx.drop 6).all Char.isDigit)
      || isAutoGenerated p
  | _ => false

/-- Should this constant be analysed as an authored CLAIM?

    Theorems, obviously.  But also a `def` WHOSE TYPE IS A PROP -- because that
    is the AGENTS.md 1a def-disguise, and a theorem-only pass is blind to exactly
    the shape that rule exists to forbid.  `theorem X : True := trivial` becomes
    invisible to every vacuity detector the moment it is re-declared as a `def`,
    which is why 1a names the move explicitly.

    Two exclusions, both necessary or the signal drowns:

    * FIELD PROJECTIONS.  A Prop-valued class field generates a `DefnInfo` whose
      type is a Prop (`C.some_hypothesis : forall inst, ...`), so admitting defs
      without this filter adds every hypothesis field of every class in the
      module -- and those are declarations of an assumption, not claims about it.
    * INSTANCES.  Same argument: an `instance : C M` asserts inhabitation, and
      whether that is honest is the conjecture-carrier question (3b-tax), a
      different audit from this one.

    Measured 2026-08-30: `QOU.Information.toffoli_transfer_matrix` -- adjudicated
    `genuine` in the vacuity ledger, and a `def` -- was reported by its module as
    0 of 3 analysable declarations, i.e. the pass could not see the finding at
    all. It is now seen. -/
def isAuthoredClaim (env : Environment) (n : Name) (ci : ConstantInfo) : MetaM Bool := do
  if ci.isTheorem then return true
  match ci with
  | .defnInfo _ =>
      if isFieldProjection env n then return false
      if (<- Lean.Meta.isInstance n) then return false
      isProp ci.type
  | _ => return false

structure Row where
  decl         : Name
  typeForeign  : Array Name
  typeLocal    : Array Name
  valueForeign : Array Name
  defeq        : Bool
  isRfl        : Bool
  onlyProjects : Bool

/-- Analyse SEVERAL modules in ONE pass over the environment.

    `env.constants` holds every imported constant -- ~300k with Mathlib in the
    cone -- so calling `analyzeModule` per module walks all of them once PER
    MODULE. One pass, bucketed by module, removes that redundancy.

    (An 8-module per-module run went ~20 min without emitting and was then
    killed, so it is not known whether it would have finished; the redundant
    traversal is real either way.) -/
def analyzeModules (mods : List Name) : MetaM (Array (Name × Array Row)) := do
  let env <- getEnv
  let want : Std.HashSet Name := mods.foldl (fun s m => s.insert m) {}
  let mut acc : Std.HashMap Name (Array Row) := {}
  for m in mods do acc := acc.insert m #[]
  for (n, ci) in env.constants.toList do
    let some self := modOf env n | continue
    unless want.contains self do continue
    if n.isInternal then continue
    if isAutoGenerated n then continue
    unless (<- isAuthoredClaim env n ci) do continue
    let tf := foreignCorpusConsts env self ci.type
    let tl := localConsts env self ci.type
    let vf := match ci.value? with
      | some v => foreignCorpusConsts env self v
      | none   => #[]
    let dq <- withOptions (·.setNat `maxHeartbeats 20000) <| defeqCollapse ci.type
    let rf := match ci.value? with | some v => valueIsRfl v | none => false
    let op := match ci.value? with
      | some v => valueOnlyProjects env self v
      | none   => false
    let row : Row := { decl := n, typeForeign := tf, typeLocal := tl,
                       valueForeign := vf, defeq := dq, isRfl := rf,
                       onlyProjects := op }
    acc := acc.insert self ((acc.getD self #[]).push row)
  return mods.toArray.map fun m => (m, acc.getD m #[])

def analyzeModule (self : Name) : MetaM (Array Row) := do
  let env <- getEnv
  let mut rows := #[]
  for (n, ci) in env.constants.toList do
    if modOf env n != some self then continue
    if n.isInternal then continue
    unless (<- isAuthoredClaim env n ci) do continue
    -- Compiler-generated equation/match lemmas are definitional BY DESIGN
    -- (`foo.eq_1` IS the unfolding of `foo`), so they would swamp the
    -- defeq signal with true-but-meaningless positives.  `Name.isInternal`
    -- does not cover them.
    if isAutoGenerated n then continue
    let tf := foreignCorpusConsts env self ci.type
    let tl := localConsts env self ci.type
    let vf := match ci.value? with
      | some v => foreignCorpusConsts env self v
      | none   => #[]
    let dq <- withOptions (·.setNat `maxHeartbeats 20000) <| defeqCollapse ci.type
    let rf := match ci.value? with | some v => valueIsRfl v | none => false
    let op := match ci.value? with
      | some v => valueOnlyProjects env self v
      | none   => false
    rows := rows.push { decl := n, typeForeign := tf, typeLocal := tl,
                        valueForeign := vf, defeq := dq, isRfl := rf,
                        onlyProjects := op }
  return rows

def esc (s : String) : String := s.replace "\"" "\\\""

def render (self : Name) (rows : Array Row) : String :=
  let items := rows.map fun r =>
    "{\"decl\":\"" ++ esc r.decl.toString ++ "\"," ++
    "\"type_foreign\":" ++ toString r.typeForeign.size ++ "," ++
    "\"type_local\":" ++ toString r.typeLocal.size ++ "," ++
    "\"value_foreign\":" ++ toString r.valueForeign.size ++ "," ++
    "\"local_only\":" ++ (if r.typeForeign.isEmpty && !r.typeLocal.isEmpty
                          then "true" else "false") ++ "," ++
    "\"defeq_collapse\":" ++ (if r.defeq then "true" else "false") ++ "," ++
    "\"value_is_rfl\":" ++ (if r.isRfl then "true" else "false") ++ "," ++
    "\"value_only_projects\":" ++ (if r.onlyProjects then "true" else "false") ++ "}"
  "{\"module\":\"" ++ esc self.toString ++ "\",\"decls\":[" ++
    String.intercalate "," items.toList ++ "]}"

end BorrowedNameKernel
