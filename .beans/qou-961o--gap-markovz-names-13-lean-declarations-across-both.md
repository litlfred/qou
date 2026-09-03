---
# qou-961o
title: 'GAP: markovZ names 13 Lean declarations across both conventions'
status: completed
type: task
priority: normal
created_at: 2026-08-29T08:04:35Z
updated_at: 2026-08-29T10:47:46Z
---

Measured 2026-08-29 on main (PR #5972). `grep -rn --include=*.lean "^\s*(noncomputable\s+)?(private\s+)?def\s+markovZ\b" content/` returns THIRTEEN declarations of the same name carrying two different functions:

CONVENTION D (10):
  mass-theory/markov-trace-factorization.lean:29                 markovZ (q, hq)
  mass-theory/y-lambda-recipe-from-partition.lean:143            markovZ {R} [Field R]
  lean/QOU/MathlibExt/MarkovBondRule.lean:84                     markovZ (q : R)
  lean/QOU/MassTheory/PnOffsetBarOddClass.lean:119               markovZ (q : K)
  lean/QOU/MassTheory/PnInterfaceBarStructure.lean:71            markovZ (q : K)
  lean/QOU/BraidKnot/QBetaCategoricalPrecisionLadder.lean:55      markovZ' (q : R)
  lean/QOU/BraidKnot/JonesNuclearQuotient.lean:78                markovZ (q : R)
  lean/QOU/QBeta/SingleCrossingAlwaysBinds.lean:89               markovZ (q : R)
  nuclear-interactions/q-beta-spectral-bridge.lean:36            markovZ (q : R)
  lean/QOU/Hecke/ClosedFormInterfaceFactors.lean:168             markovZ (s) = s^6/(s^4+1)   [D in sqrt-variable]

CONVENTION C (3):
  lean/QOU/BraidKnot/HoefsmitV21CosSymmetrization.lean:194       markovZ (u) = u/(u^2+1)     [the KERNEL]
  lean/QOU/QBeta/EigenphaseCarrierVacuity.lean:61                markovZ (q) = 1/(sqrt q + (sqrt q)^-1)
  nuclear-interactions/q-beta-cos-resummation.lean:63            markovZ (q) = 1/(sqrt q + (sqrt q)^-1)

At q0: z_C = 0.4993203, z_D = 0.6126880. Same name, values differing by 23%.

AGENTS.md RECORDS THIS AS "five declarations, three C, two D" AND IS STALE IN
BOTH DIRECTIONS. It names markov-trace-factorization and
QBetaCategoricalPrecisionLadder as two of the three C; both are now D. The true
figure is 13 declarations, 3 C and 10 D. Correct AGENTS.md when this closes.

WHY THIS IS NOT SIMPLY A DEFECT LIST. All three C sites ANNOUNCE THEMSELVES in
their docstrings, so `scripts/lean-markov-convention-audit.py` correctly reports
the whole Lean surface as 14 C definitions / 0 actionable / 14 deliberate. Each
has a reason to exist:
  - HoefsmitV21 markovZ is the convention-NEUTRAL kernel; the file proves
    `no_kernel_instantiation_is_conventionD` (z_D is the rescaling q^2 * kernel,
    not the kernel at any argument) and exposes markovZ_real, which IS D.
  - EigenphaseCarrierVacuity reproduces the content block's spelling verbatim
    in order to demonstrate that the carrier is vacuous.
  - q-beta-cos-resummation proves F(1/q) = -F(q), which is TRUE for C and FALSE
    for D. Its own docstring says so and says the C statement "keeps its name".

THE DEFECT IS THE NAME, NOT THE VALUE. A docstring announces the convention to a
reader who opens the file; it does nothing for a reader who sees `markovZ` in a
citation, a proof term, or a sibling file's import and assumes the canonical
one. That is exactly how the "rfl agreement with QBetaSpectralBridge.markovZ"
claim in q-beta-cos-resummation went stale when the sibling migrated -- the
file's own docstring records catching it.

PROPOSED, NOT DONE: rename the three C declarations so the name stops spanning
conventions -- markovZC (or markovZ_conventionC) for the two eigenphase files,
markovKernel for the HoefsmitV21 kernel (matching the existing
MarkovConventionSeparation.markovKernel, which is the same object under an
honest name). All three are file-local: grep finds no cross-file reference to
any of them by qualified name. Verification is `lean`-direct per AGENTS.md, NOT
`lake build` -- this container has a RESTORED .lake (marker
.lake/RESTORED-NO-TRACES present, 7268 oleans, 6990 of them mathlib) and a lake
build would evict the restore. Measured recipe that works here:

  export PATH="$HOME/.elan/bin:$PATH"
  LP=$(ls -d /home/user/qou/.lake/packages/*/.lake/build/lib/lean \
             /home/user/qou/content/*/lean/.lake/build/lib/lean | tr "\n" ":")
  cd content/quantum-observable-universe/lean && LEAN_PATH="$LP" lean <file>.lean

  Note the trailing `/lean` on each entry -- without it the path resolves to a
  directory containing only `lean/` and every import fails with "unknown module
  prefix". Verified: EigenphaseCarrierVacuity.lean exits 0 in 1m43s.

NOT done in PR #5972 because a rename touching three files needs each one
lean-verified and the session budget went to the computations/ surface, where
the finding was larger. Deliberately left rather than half-done.

SCOPED 2026-08-29 (session tender-keller): all 3 C markovZ are FILE-LOCAL (no cross-file refs) — safe to rename. Proposed: EigenphaseCarrierVacuity markovZ->markovZC (2 refs); q-beta-cos-resummation markovZ->markovZC (9 refs); HoefsmitV21CosSymmetrization markovZ->cosKernel (10 refs, it is the convention-neutral kernel u/(u²+1)). Leaves bare markovZ = convention D (10 sites, consistent). CAUTION: surgical word-boundary rename needed — bare replace_all corrupts substrings like markovZD_eq_sq_mul_kernel. Then correct AGENTS.md stale '5 decls/3C/2D'. Awaiting owner nod (touches deliberately-documented decls; audit says 0-actionable so hygiene not correctness).

FIX APPLIED 2026-08-29 (session tender-keller): renamed the 3 C markovZ — EigenphaseCarrierVacuity + q-beta-cos-resummation -> markovZC; HoefsmitV21CosSymmetrization kernel -> cosKernel. Word-boundary rename (markovZ_real/legacy/markovZD substrings + QBetaSpectralBridge.markovZ untouched). All 3 lean-direct GREEN (exit 0). AGENTS.md resolution note added. PR pending; close on merge.
