/-!
# Free-Nucleon Precision-Straddle Defect (`qou-1kq0`)

This module formalizes the algebraic structure of the free-nucleon precision-straddle
defect identified in `path_b_defect_binding_probe.py` (`qou-1kq0`):

1. **Zero binding energy of a free nucleon (`free_proton_binding_vanishes_iff_precision_matched`):**
   In the nuclear mass-defect definition
   `B(Z, N) = Z * M_H + N * M_n - M(Z, N)`,
   the free proton `(Z = 1, N = 0)` has `B(1, 0) = M_H_constituent - M_H_table`.
   This vanishes if and only if both terms are evaluated at matching precision.

2. **Spurious residual from mixed-precision straddle (`free_proton_straddle_spurious_residual_and_error`):**
   When `M_H_constituent` is promoted to 50-dps CODATA precision while `M_AME["p"]`
   remains a truncated 11-digit float literal `M_H_exact - delta_trunc` (`delta_trunc > 0`),
   the free proton acquires a nonzero spurious binding energy `B(1, 0) = delta_trunc > 0`
   (`1.2706900633929763e-06 MeV`) and a relative error of `-100%`.

3. **Unmodified-code baseline vs stale-witness baseline (`unstraddled_baseline_diff_cancels_preexisting_defect`):**
   Diffing a modified run against a stale committed witness attributes pre-existing
   drift (`bUnmodified - bStaleCommitted = bUnmodified > 0`) to the new change, whereas
   diffing against a fresh run of the unmodified code cancels pre-existing drift (`0`).
-/

namespace QOU.MassTheory.FreeNucleonPrecisionStraddleDefect

/-- Mass-defect binding energy `Z * mH + N * mn - mMeasured`. -/
def bindingDefect (Z N mH mn mMeasured : Int) : Int :=
  Z * mH + N * mn - mMeasured

/-- Free-proton (`Z = 1, N = 0`) binding energy under constituent vs table mass inputs. -/
def straddleFreeProtonBinding (mHExact mHTrunc : Int) : Int :=
  bindingDefect 1 0 mHExact 0 mHTrunc

/-- For the free proton (`Z = 1, N = 0`), the mass-defect binding energy is independent
    of the neutron mass `mn`, equals `mHExact - mHTrunc`, and vanishes if and only if
    constituent and measured hydrogen masses match in precision (`qou-1kq0`). -/
theorem free_proton_binding_vanishes_iff_precision_matched
    (mHExact mHTrunc mn : Int) :
    bindingDefect 1 0 mHExact mn mHTrunc = mHExact - mHTrunc ∧
    (bindingDefect 1 0 mHExact mn mHTrunc = 0 ↔ mHExact = mHTrunc) := by
  have heval : bindingDefect 1 0 mHExact mn mHTrunc = mHExact - mHTrunc := by
    unfold bindingDefect
    omega
  have hiff : bindingDefect 1 0 mHExact mn mHTrunc = 0 ↔ mHExact = mHTrunc := by
    rw [heval]
    omega
  exact ⟨heval, hiff⟩

/-- Truncating the table literal by `deltaTrunc > 0` below the full-precision constituent
    sum induces a strictly positive spurious binding residual `deltaTrunc` and a negative
    prediction residual `-deltaTrunc` on the free proton (`qou-1kq0`). -/
theorem free_proton_straddle_spurious_residual_and_error
    (mHExact deltaTrunc : Int) (hdelta : deltaTrunc > 0) :
    straddleFreeProtonBinding mHExact (mHExact - deltaTrunc) = deltaTrunc ∧
    straddleFreeProtonBinding mHExact (mHExact - deltaTrunc) > 0 ∧
    (0 - straddleFreeProtonBinding mHExact (mHExact - deltaTrunc)) = -deltaTrunc := by
  have hres : straddleFreeProtonBinding mHExact (mHExact - deltaTrunc) = deltaTrunc := by
    unfold straddleFreeProtonBinding bindingDefect
    omega
  have hpos : straddleFreeProtonBinding mHExact (mHExact - deltaTrunc) > 0 := by
    rw [hres]
    exact hdelta
  have herr : 0 - straddleFreeProtonBinding mHExact (mHExact - deltaTrunc) = -deltaTrunc := by
    rw [hres]
    omega
  exact ⟨hres, hpos, herr⟩

/-- Diffing against a fresh unmodified run cancels pre-existing precision-straddle
    residuals (`0`), whereas diffing against a stale zero witness mis-attributes
    the entire pre-existing residual `bUnmodified` to the new change (`qou-1kq0`). -/
theorem unstraddled_baseline_diff_cancels_preexisting_defect
    (bUnmodified bModified bStaleCommitted : Int)
    (hpre : bUnmodified = bModified)
    (hstale : bStaleCommitted = 0)
    (hnz : bUnmodified > 0) :
    bModified - bUnmodified = 0 ∧
    bModified - bStaleCommitted = bUnmodified ∧
    bModified - bStaleCommitted > 0 := by
  have hfresh : bModified - bUnmodified = 0 := by
    omega
  have hcommitted : bModified - bStaleCommitted = bUnmodified := by
    omega
  have hpos : bModified - bStaleCommitted > 0 := by
    omega
  exact ⟨hfresh, hcommitted, hpos⟩

end QOU.MassTheory.FreeNucleonPrecisionStraddleDefect
