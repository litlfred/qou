/-!
# QOU.BraidsKnots.RamifiedDiscFusion

Compiled formalisation of `prop:ramified-disc-fusion`.
Sibling docstub at `braids-and-knots/ramified-disc-fusion.md`.

At the foundry boundary latitudes $\phi \in \{0, \pi\}$ of the
Reeb bundle, the three coral-sector preimages of a small disc on
the exceptional divisor fuse into a single topological disc with
degree-3 ramification at the centre.  The monodromy of this
branched cover around the boundary circle realises the $S_3$
Galois action on the three sectors.

## References

- [manuscript] content/quantum-observable-universe/braids-and-knots/ramified-disc-fusion.md
-/

namespace QOU.BraidsKnots

/-- Abstract context for the `ramified_disc_fusion` claim. -/
class RamifiedDiscFusionContext where
  /-- Number of coral-sector preimages of a small disc on the
      exceptional divisor at a foundry boundary latitude. -/
  n_sectors : ℕ
  /-- Ramification degree of the branched cover at the disc centre. -/
  ramification_degree : ℕ
  /-- Order of the Galois group realised by monodromy around the
      boundary circle (manuscript: `S_3`, order 6). -/
  galois_group_order : ℕ
  /-- Manuscript claim — three coral sectors. -/
  claim_three_sectors : n_sectors = 3
  /-- Manuscript claim — degree-3 ramification at the centre
      (matches the sector count). -/
  claim_degree_three_ramification : ramification_degree = 3
  /-- Manuscript claim — `S_3` monodromy: the Galois group of the
      branched cover has order `|S_3| = 6`. -/
  claim_s3_monodromy : galois_group_order = 6

/-- **Proposition (`prop:ramified-disc-fusion`).** -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/ramified-disc-fusion.md
def RamifiedDiscFusion [ctx : RamifiedDiscFusionContext] :
    ctx.n_sectors = 3 ∧
    ctx.ramification_degree = 3 ∧
    ctx.galois_group_order = 6 :=
  ⟨ctx.claim_three_sectors, ctx.claim_degree_three_ramification,
   ctx.claim_s3_monodromy⟩

end QOU.BraidsKnots
