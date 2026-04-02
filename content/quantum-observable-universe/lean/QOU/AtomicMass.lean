import Mathlib.Data.Real.Basic
import QOU.HadronicMass

namespace QOU.AtomicMass

-- CODATA 2022 full-precision constituent masses (MeV)
noncomputable def m_p : Real := 938.27208943
noncomputable def m_n : Real := 939.56542194
noncomputable def m_e : Real := 0.51099895069

noncomputable def atomic_mass (Z N : Nat) (BperA : Real) : Real :=
  (Z : Real) * m_p + (N : Real) * m_n + (Z : Real) * m_e - ((Z : Real) + (N : Real)) * BperA

structure AtomicMassDatum where
  Z : Nat
  N : Nat
  BperA : Real
  observed : Real
  absBound : Real
  pctBound : Real

noncomputable def AtomicMassDatum.qouMass (d : AtomicMassDatum) : Real :=
  atomic_mass d.Z d.N d.BperA

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def h : AtomicMassDatum where
  Z := 1; N := 0; BperA := 0.0000
  observed := 938.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_h : |h.qouMass - h.observed| < h.absBound := by
  unfold AtomicMassDatum.qouMass h atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_h :
    |h.qouMass - h.observed| / h.observed * 100 < h.pctBound := by
  unfold AtomicMassDatum.qouMass h atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def he : AtomicMassDatum where
  Z := 2; N := 2; BperA := 7.0739
  observed := 3728.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_he : |he.qouMass - he.observed| < he.absBound := by
  unfold AtomicMassDatum.qouMass he atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_he :
    |he.qouMass - he.observed| / he.observed * 100 < he.pctBound := by
  unfold AtomicMassDatum.qouMass he atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def li : AtomicMassDatum where
  Z := 3; N := 4; BperA := 5.6063
  observed := 6535.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_li : |li.qouMass - li.observed| < li.absBound := by
  unfold AtomicMassDatum.qouMass li atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_li :
    |li.qouMass - li.observed| / li.observed * 100 < li.pctBound := by
  unfold AtomicMassDatum.qouMass li atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def be : AtomicMassDatum where
  Z := 4; N := 5; BperA := 6.4628
  observed := 8394.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_be : |be.qouMass - be.observed| < be.absBound := by
  unfold AtomicMassDatum.qouMass be atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_be :
    |be.qouMass - be.observed| / be.observed * 100 < be.pctBound := by
  unfold AtomicMassDatum.qouMass be atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def b : AtomicMassDatum where
  Z := 5; N := 6; BperA := 6.9277
  observed := 10255.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_b : |b.qouMass - b.observed| < b.absBound := by
  unfold AtomicMassDatum.qouMass b atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_b :
    |b.qouMass - b.observed| / b.observed * 100 < b.pctBound := by
  unfold AtomicMassDatum.qouMass b atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def c : AtomicMassDatum where
  Z := 6; N := 6; BperA := 7.6801
  observed := 11177.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_c : |c.qouMass - c.observed| < c.absBound := by
  unfold AtomicMassDatum.qouMass c atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_c :
    |c.qouMass - c.observed| / c.observed * 100 < c.pctBound := by
  unfold AtomicMassDatum.qouMass c atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def n : AtomicMassDatum where
  Z := 7; N := 7; BperA := 7.4756
  observed := 13043.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_n : |n.qouMass - n.observed| < n.absBound := by
  unfold AtomicMassDatum.qouMass n atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_n :
    |n.qouMass - n.observed| / n.observed * 100 < n.pctBound := by
  unfold AtomicMassDatum.qouMass n atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def o : AtomicMassDatum where
  Z := 8; N := 8; BperA := 7.9762
  observed := 14899.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_o : |o.qouMass - o.observed| < o.absBound := by
  unfold AtomicMassDatum.qouMass o atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_o :
    |o.qouMass - o.observed| / o.observed * 100 < o.pctBound := by
  unfold AtomicMassDatum.qouMass o atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def f : AtomicMassDatum where
  Z := 9; N := 10; BperA := 7.7790
  observed := 17696.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_f : |f.qouMass - f.observed| < f.absBound := by
  unfold AtomicMassDatum.qouMass f atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_f :
    |f.qouMass - f.observed| / f.observed * 100 < f.pctBound := by
  unfold AtomicMassDatum.qouMass f atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ne : AtomicMassDatum where
  Z := 10; N := 10; BperA := 8.0325
  observed := 18622.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ne : |ne.qouMass - ne.observed| < ne.absBound := by
  unfold AtomicMassDatum.qouMass ne atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ne :
    |ne.qouMass - ne.observed| / ne.observed * 100 < ne.pctBound := by
  unfold AtomicMassDatum.qouMass ne atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def na : AtomicMassDatum where
  Z := 11; N := 12; BperA := 8.1115
  observed := 21414.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_na : |na.qouMass - na.observed| < na.absBound := by
  unfold AtomicMassDatum.qouMass na atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_na :
    |na.qouMass - na.observed| / na.observed * 100 < na.pctBound := by
  unfold AtomicMassDatum.qouMass na atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def mg : AtomicMassDatum where
  Z := 12; N := 12; BperA := 8.2607
  observed := 22341.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_mg : |mg.qouMass - mg.observed| < mg.absBound := by
  unfold AtomicMassDatum.qouMass mg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_mg :
    |mg.qouMass - mg.observed| / mg.observed * 100 < mg.pctBound := by
  unfold AtomicMassDatum.qouMass mg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def al : AtomicMassDatum where
  Z := 13; N := 14; BperA := 8.3316
  observed := 25133.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_al : |al.qouMass - al.observed| < al.absBound := by
  unfold AtomicMassDatum.qouMass al atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_al :
    |al.qouMass - al.observed| / al.observed * 100 < al.pctBound := by
  unfold AtomicMassDatum.qouMass al atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def si : AtomicMassDatum where
  Z := 14; N := 14; BperA := 8.4477
  observed := 26060.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_si : |si.qouMass - si.observed| < si.absBound := by
  unfold AtomicMassDatum.qouMass si atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_si :
    |si.qouMass - si.observed| / si.observed * 100 < si.pctBound := by
  unfold AtomicMassDatum.qouMass si atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def p : AtomicMassDatum where
  Z := 15; N := 16; BperA := 8.4812
  observed := 28851.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_p : |p.qouMass - p.observed| < p.absBound := by
  unfold AtomicMassDatum.qouMass p atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_p :
    |p.qouMass - p.observed| / p.observed * 100 < p.pctBound := by
  unfold AtomicMassDatum.qouMass p atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def s : AtomicMassDatum where
  Z := 16; N := 16; BperA := 8.4932
  observed := 29781.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_s : |s.qouMass - s.observed| < s.absBound := by
  unfold AtomicMassDatum.qouMass s atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_s :
    |s.qouMass - s.observed| / s.observed * 100 < s.pctBound := by
  unfold AtomicMassDatum.qouMass s atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def cl : AtomicMassDatum where
  Z := 17; N := 18; BperA := 8.5203
  observed := 32573.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cl : |cl.qouMass - cl.observed| < cl.absBound := by
  unfold AtomicMassDatum.qouMass cl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cl :
    |cl.qouMass - cl.observed| / cl.observed * 100 < cl.pctBound := by
  unfold AtomicMassDatum.qouMass cl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ar : AtomicMassDatum where
  Z := 18; N := 22; BperA := 8.5954
  observed := 37224.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ar : |ar.qouMass - ar.observed| < ar.absBound := by
  unfold AtomicMassDatum.qouMass ar atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ar :
    |ar.qouMass - ar.observed| / ar.observed * 100 < ar.pctBound := by
  unfold AtomicMassDatum.qouMass ar atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def k : AtomicMassDatum where
  Z := 19; N := 20; BperA := 8.5570
  observed := 36294.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_k : |k.qouMass - k.observed| < k.absBound := by
  unfold AtomicMassDatum.qouMass k atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_k :
    |k.qouMass - k.observed| / k.observed * 100 < k.pctBound := by
  unfold AtomicMassDatum.qouMass k atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ca : AtomicMassDatum where
  Z := 20; N := 20; BperA := 8.5513
  observed := 37224.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ca : |ca.qouMass - ca.observed| < ca.absBound := by
  unfold AtomicMassDatum.qouMass ca atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ca :
    |ca.qouMass - ca.observed| / ca.observed * 100 < ca.pctBound := by
  unfold AtomicMassDatum.qouMass ca atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def sc : AtomicMassDatum where
  Z := 21; N := 24; BperA := 8.6190
  observed := 41876.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_sc : |sc.qouMass - sc.observed| < sc.absBound := by
  unfold AtomicMassDatum.qouMass sc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_sc :
    |sc.qouMass - sc.observed| / sc.observed * 100 < sc.pctBound := by
  unfold AtomicMassDatum.qouMass sc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ti : AtomicMassDatum where
  Z := 22; N := 26; BperA := 8.7230
  observed := 44663.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ti : |ti.qouMass - ti.observed| < ti.absBound := by
  unfold AtomicMassDatum.qouMass ti atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ti :
    |ti.qouMass - ti.observed| / ti.observed * 100 < ti.pctBound := by
  unfold AtomicMassDatum.qouMass ti atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def v : AtomicMassDatum where
  Z := 23; N := 28; BperA := 8.7420
  observed := 47454.0
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_v : |v.qouMass - v.observed| < v.absBound := by
  unfold AtomicMassDatum.qouMass v atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_v :
    |v.qouMass - v.observed| / v.observed * 100 < v.pctBound := by
  unfold AtomicMassDatum.qouMass v atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def cr : AtomicMassDatum where
  Z := 24; N := 28; BperA := 8.7760
  observed := 48382.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cr : |cr.qouMass - cr.observed| < cr.absBound := by
  unfold AtomicMassDatum.qouMass cr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cr :
    |cr.qouMass - cr.observed| / cr.observed * 100 < cr.pctBound := by
  unfold AtomicMassDatum.qouMass cr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def mn : AtomicMassDatum where
  Z := 25; N := 30; BperA := 8.7649
  observed := 51174.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_mn : |mn.qouMass - mn.observed| < mn.absBound := by
  unfold AtomicMassDatum.qouMass mn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_mn :
    |mn.qouMass - mn.observed| / mn.observed * 100 < mn.pctBound := by
  unfold AtomicMassDatum.qouMass mn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def fe : AtomicMassDatum where
  Z := 26; N := 30; BperA := 8.7903
  observed := 52103.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_fe : |fe.qouMass - fe.observed| < fe.absBound := by
  unfold AtomicMassDatum.qouMass fe atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_fe :
    |fe.qouMass - fe.observed| / fe.observed * 100 < fe.pctBound := by
  unfold AtomicMassDatum.qouMass fe atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def co : AtomicMassDatum where
  Z := 27; N := 32; BperA := 8.7680
  observed := 54895.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_co : |co.qouMass - co.observed| < co.absBound := by
  unfold AtomicMassDatum.qouMass co atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_co :
    |co.qouMass - co.observed| / co.observed * 100 < co.pctBound := by
  unfold AtomicMassDatum.qouMass co atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ni : AtomicMassDatum where
  Z := 28; N := 30; BperA := 8.7322
  observed := 53966.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ni : |ni.qouMass - ni.observed| < ni.absBound := by
  unfold AtomicMassDatum.qouMass ni atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ni :
    |ni.qouMass - ni.observed| / ni.observed * 100 < ni.pctBound := by
  unfold AtomicMassDatum.qouMass ni atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def cu : AtomicMassDatum where
  Z := 29; N := 34; BperA := 8.7522
  observed := 58618.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cu : |cu.qouMass - cu.observed| < cu.absBound := by
  unfold AtomicMassDatum.qouMass cu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cu :
    |cu.qouMass - cu.observed| / cu.observed * 100 < cu.pctBound := by
  unfold AtomicMassDatum.qouMass cu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def zn : AtomicMassDatum where
  Z := 30; N := 34; BperA := 8.7357
  observed := 59549.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_zn : |zn.qouMass - zn.observed| < zn.absBound := by
  unfold AtomicMassDatum.qouMass zn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_zn :
    |zn.qouMass - zn.observed| / zn.observed * 100 < zn.pctBound := by
  unfold AtomicMassDatum.qouMass zn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ga : AtomicMassDatum where
  Z := 31; N := 38; BperA := 8.7246
  observed := 64203.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ga : |ga.qouMass - ga.observed| < ga.absBound := by
  unfold AtomicMassDatum.qouMass ga atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ga :
    |ga.qouMass - ga.observed| / ga.observed * 100 < ga.pctBound := by
  unfold AtomicMassDatum.qouMass ga atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ge : AtomicMassDatum where
  Z := 32; N := 42; BperA := 8.7264
  observed := 68857.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ge : |ge.qouMass - ge.observed| < ge.absBound := by
  unfold AtomicMassDatum.qouMass ge atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ge :
    |ge.qouMass - ge.observed| / ge.observed * 100 < ge.pctBound := by
  unfold AtomicMassDatum.qouMass ge atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def as_ : AtomicMassDatum where
  Z := 33; N := 42; BperA := 8.7010
  observed := 69789.0
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_as_ : |as_.qouMass - as_.observed| < as_.absBound := by
  unfold AtomicMassDatum.qouMass as_ atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_as_ :
    |as_.qouMass - as_.observed| / as_.observed * 100 < as_.pctBound := by
  unfold AtomicMassDatum.qouMass as_ atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def se : AtomicMassDatum where
  Z := 34; N := 46; BperA := 8.7110
  observed := 74441.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_se : |se.qouMass - se.observed| < se.absBound := by
  unfold AtomicMassDatum.qouMass se atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_se :
    |se.qouMass - se.observed| / se.observed * 100 < se.pctBound := by
  unfold AtomicMassDatum.qouMass se atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def br : AtomicMassDatum where
  Z := 35; N := 44; BperA := 8.6961
  observed := 73511.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_br : |br.qouMass - br.observed| < br.absBound := by
  unfold AtomicMassDatum.qouMass br atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_br :
    |br.qouMass - br.observed| / br.observed * 100 < br.pctBound := by
  unfold AtomicMassDatum.qouMass br atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def kr : AtomicMassDatum where
  Z := 36; N := 48; BperA := 8.7172
  observed := 78163.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_kr : |kr.qouMass - kr.observed| < kr.absBound := by
  unfold AtomicMassDatum.qouMass kr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_kr :
    |kr.qouMass - kr.observed| / kr.observed * 100 < kr.pctBound := by
  unfold AtomicMassDatum.qouMass kr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def rb : AtomicMassDatum where
  Z := 37; N := 48; BperA := 8.6974
  observed := 79094.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_rb : |rb.qouMass - rb.observed| < rb.absBound := by
  unfold AtomicMassDatum.qouMass rb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_rb :
    |rb.qouMass - rb.observed| / rb.observed * 100 < rb.pctBound := by
  unfold AtomicMassDatum.qouMass rb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def sr : AtomicMassDatum where
  Z := 38; N := 50; BperA := 8.7326
  observed := 81883.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_sr : |sr.qouMass - sr.observed| < sr.absBound := by
  unfold AtomicMassDatum.qouMass sr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_sr :
    |sr.qouMass - sr.observed| / sr.observed * 100 < sr.pctBound := by
  unfold AtomicMassDatum.qouMass sr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def y : AtomicMassDatum where
  Z := 39; N := 50; BperA := 8.7138
  observed := 82815.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_y : |y.qouMass - y.observed| < y.absBound := by
  unfold AtomicMassDatum.qouMass y atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_y :
    |y.qouMass - y.observed| / y.observed * 100 < y.pctBound := by
  unfold AtomicMassDatum.qouMass y atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def zr : AtomicMassDatum where
  Z := 40; N := 50; BperA := 8.7098
  observed := 83745.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_zr : |zr.qouMass - zr.observed| < zr.absBound := by
  unfold AtomicMassDatum.qouMass zr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_zr :
    |zr.qouMass - zr.observed| / zr.observed * 100 < zr.pctBound := by
  unfold AtomicMassDatum.qouMass zr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def nb : AtomicMassDatum where
  Z := 41; N := 52; BperA := 8.6641
  observed := 86541.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_nb : |nb.qouMass - nb.observed| < nb.absBound := by
  unfold AtomicMassDatum.qouMass nb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_nb :
    |nb.qouMass - nb.observed| / nb.observed * 100 < nb.pctBound := by
  unfold AtomicMassDatum.qouMass nb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def mo : AtomicMassDatum where
  Z := 42; N := 56; BperA := 8.6353
  observed := 91198.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_mo : |mo.qouMass - mo.observed| < mo.absBound := by
  unfold AtomicMassDatum.qouMass mo atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_mo :
    |mo.qouMass - mo.observed| / mo.observed * 100 < mo.pctBound := by
  unfold AtomicMassDatum.qouMass mo atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def tc : AtomicMassDatum where
  Z := 43; N := 55; BperA := 8.5937
  observed := 91201.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_tc : |tc.qouMass - tc.observed| < tc.absBound := by
  unfold AtomicMassDatum.qouMass tc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_tc :
    |tc.qouMass - tc.observed| / tc.observed * 100 < tc.pctBound := by
  unfold AtomicMassDatum.qouMass tc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ru : AtomicMassDatum where
  Z := 44; N := 58; BperA := 8.6070
  observed := 94923.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ru : |ru.qouMass - ru.observed| < ru.absBound := by
  unfold AtomicMassDatum.qouMass ru atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ru :
    |ru.qouMass - ru.observed| / ru.observed * 100 < ru.pctBound := by
  unfold AtomicMassDatum.qouMass ru atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def rh : AtomicMassDatum where
  Z := 45; N := 58; BperA := 8.5843
  observed := 95855.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_rh : |rh.qouMass - rh.observed| < rh.absBound := by
  unfold AtomicMassDatum.qouMass rh atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_rh :
    |rh.qouMass - rh.observed| / rh.observed * 100 < rh.pctBound := by
  unfold AtomicMassDatum.qouMass rh atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def pd : AtomicMassDatum where
  Z := 46; N := 60; BperA := 8.5670
  observed := 98649.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_pd : |pd.qouMass - pd.observed| < pd.absBound := by
  unfold AtomicMassDatum.qouMass pd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_pd :
    |pd.qouMass - pd.observed| / pd.observed * 100 < pd.pctBound := by
  unfold AtomicMassDatum.qouMass pd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ag : AtomicMassDatum where
  Z := 47; N := 60; BperA := 8.5536
  observed := 99581.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ag : |ag.qouMass - ag.observed| < ag.absBound := by
  unfold AtomicMassDatum.qouMass ag atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ag :
    |ag.qouMass - ag.observed| / ag.observed * 100 < ag.pctBound := by
  unfold AtomicMassDatum.qouMass ag atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def cd : AtomicMassDatum where
  Z := 48; N := 66; BperA := 8.5398
  observed := 106099.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cd : |cd.qouMass - cd.observed| < cd.absBound := by
  unfold AtomicMassDatum.qouMass cd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cd :
    |cd.qouMass - cd.observed| / cd.observed * 100 < cd.pctBound := by
  unfold AtomicMassDatum.qouMass cd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def in_ : AtomicMassDatum where
  Z := 49; N := 66; BperA := 8.5160
  observed := 107032.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_in_ : |in_.qouMass - in_.observed| < in_.absBound := by
  unfold AtomicMassDatum.qouMass in_ atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_in_ :
    |in_.qouMass - in_.observed| / in_.observed * 100 < in_.pctBound := by
  unfold AtomicMassDatum.qouMass in_ atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def sn : AtomicMassDatum where
  Z := 50; N := 70; BperA := 8.5050
  observed := 111688.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_sn : |sn.qouMass - sn.observed| < sn.absBound := by
  unfold AtomicMassDatum.qouMass sn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_sn :
    |sn.qouMass - sn.observed| / sn.observed * 100 < sn.pctBound := by
  unfold AtomicMassDatum.qouMass sn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def sb : AtomicMassDatum where
  Z := 51; N := 70; BperA := 8.4820
  observed := 112621.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_sb : |sb.qouMass - sb.observed| < sb.absBound := by
  unfold AtomicMassDatum.qouMass sb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_sb :
    |sb.qouMass - sb.observed| / sb.observed * 100 < sb.pctBound := by
  unfold AtomicMassDatum.qouMass sb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def te : AtomicMassDatum where
  Z := 52; N := 78; BperA := 8.4390
  observed := 121005.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_te : |te.qouMass - te.observed| < te.absBound := by
  unfold AtomicMassDatum.qouMass te atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_te :
    |te.qouMass - te.observed| / te.observed * 100 < te.pctBound := by
  unfold AtomicMassDatum.qouMass te atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def i : AtomicMassDatum where
  Z := 53; N := 74; BperA := 8.4455
  observed := 118210.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_i : |i.qouMass - i.observed| < i.absBound := by
  unfold AtomicMassDatum.qouMass i atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_i :
    |i.qouMass - i.observed| / i.observed * 100 < i.pctBound := by
  unfold AtomicMassDatum.qouMass i atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def xe : AtomicMassDatum where
  Z := 54; N := 78; BperA := 8.4275
  observed := 122868.0
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_xe : |xe.qouMass - xe.observed| < xe.absBound := by
  unfold AtomicMassDatum.qouMass xe atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_xe :
    |xe.qouMass - xe.observed| / xe.observed * 100 < xe.pctBound := by
  unfold AtomicMassDatum.qouMass xe atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def cs : AtomicMassDatum where
  Z := 55; N := 78; BperA := 8.4100
  observed := 123800.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cs : |cs.qouMass - cs.observed| < cs.absBound := by
  unfold AtomicMassDatum.qouMass cs atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cs :
    |cs.qouMass - cs.observed| / cs.observed * 100 < cs.pctBound := by
  unfold AtomicMassDatum.qouMass cs atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ba : AtomicMassDatum where
  Z := 56; N := 82; BperA := 8.3937
  observed := 128457.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ba : |ba.qouMass - ba.observed| < ba.absBound := by
  unfold AtomicMassDatum.qouMass ba atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ba :
    |ba.qouMass - ba.observed| / ba.observed * 100 < ba.pctBound := by
  unfold AtomicMassDatum.qouMass ba atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def la : AtomicMassDatum where
  Z := 57; N := 82; BperA := 8.3780
  observed := 129390.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_la : |la.qouMass - la.observed| < la.absBound := by
  unfold AtomicMassDatum.qouMass la atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_la :
    |la.qouMass - la.observed| / la.observed * 100 < la.pctBound := by
  unfold AtomicMassDatum.qouMass la atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ce : AtomicMassDatum where
  Z := 58; N := 82; BperA := 8.3765
  observed := 130321.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ce : |ce.qouMass - ce.observed| < ce.absBound := by
  unfold AtomicMassDatum.qouMass ce atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ce :
    |ce.qouMass - ce.observed| / ce.observed * 100 < ce.pctBound := by
  unfold AtomicMassDatum.qouMass ce atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def pr : AtomicMassDatum where
  Z := 59; N := 82; BperA := 8.3540
  observed := 131254.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_pr : |pr.qouMass - pr.observed| < pr.absBound := by
  unfold AtomicMassDatum.qouMass pr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_pr :
    |pr.qouMass - pr.observed| / pr.observed * 100 < pr.pctBound := by
  unfold AtomicMassDatum.qouMass pr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def nd : AtomicMassDatum where
  Z := 60; N := 82; BperA := 8.3460
  observed := 132186.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_nd : |nd.qouMass - nd.observed| < nd.absBound := by
  unfold AtomicMassDatum.qouMass nd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_nd :
    |nd.qouMass - nd.observed| / nd.observed * 100 < nd.pctBound := by
  unfold AtomicMassDatum.qouMass nd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def pm : AtomicMassDatum where
  Z := 61; N := 84; BperA := 8.3040
  observed := 134985.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_pm : |pm.qouMass - pm.observed| < pm.absBound := by
  unfold AtomicMassDatum.qouMass pm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_pm :
    |pm.qouMass - pm.observed| / pm.observed * 100 < pm.pctBound := by
  unfold AtomicMassDatum.qouMass pm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def sm : AtomicMassDatum where
  Z := 62; N := 90; BperA := 8.2440
  observed := 141512.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_sm : |sm.qouMass - sm.observed| < sm.absBound := by
  unfold AtomicMassDatum.qouMass sm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_sm :
    |sm.qouMass - sm.observed| / sm.observed * 100 < sm.pctBound := by
  unfold AtomicMassDatum.qouMass sm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def eu : AtomicMassDatum where
  Z := 63; N := 90; BperA := 8.2290
  observed := 142445.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_eu : |eu.qouMass - eu.observed| < eu.absBound := by
  unfold AtomicMassDatum.qouMass eu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_eu :
    |eu.qouMass - eu.observed| / eu.observed * 100 < eu.pctBound := by
  unfold AtomicMassDatum.qouMass eu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def gd : AtomicMassDatum where
  Z := 64; N := 94; BperA := 8.2140
  observed := 147103.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_gd : |gd.qouMass - gd.observed| < gd.absBound := by
  unfold AtomicMassDatum.qouMass gd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_gd :
    |gd.qouMass - gd.observed| / gd.observed * 100 < gd.pctBound := by
  unfold AtomicMassDatum.qouMass gd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def tb : AtomicMassDatum where
  Z := 65; N := 94; BperA := 8.1990
  observed := 148036.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_tb : |tb.qouMass - tb.observed| < tb.absBound := by
  unfold AtomicMassDatum.qouMass tb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_tb :
    |tb.qouMass - tb.observed| / tb.observed * 100 < tb.pctBound := by
  unfold AtomicMassDatum.qouMass tb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def dy : AtomicMassDatum where
  Z := 66; N := 98; BperA := 8.1865
  observed := 152694.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_dy : |dy.qouMass - dy.observed| < dy.absBound := by
  unfold AtomicMassDatum.qouMass dy atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_dy :
    |dy.qouMass - dy.observed| / dy.observed * 100 < dy.pctBound := by
  unfold AtomicMassDatum.qouMass dy atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ho : AtomicMassDatum where
  Z := 67; N := 98; BperA := 8.1710
  observed := 153627.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ho : |ho.qouMass - ho.observed| < ho.absBound := by
  unfold AtomicMassDatum.qouMass ho atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ho :
    |ho.qouMass - ho.observed| / ho.observed * 100 < ho.pctBound := by
  unfold AtomicMassDatum.qouMass ho atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def er : AtomicMassDatum where
  Z := 68; N := 98; BperA := 8.1690
  observed := 154558.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_er : |er.qouMass - er.observed| < er.absBound := by
  unfold AtomicMassDatum.qouMass er atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_er :
    |er.qouMass - er.observed| / er.observed * 100 < er.pctBound := by
  unfold AtomicMassDatum.qouMass er atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def tm : AtomicMassDatum where
  Z := 69; N := 100; BperA := 8.1460
  observed := 157355.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_tm : |tm.qouMass - tm.observed| < tm.absBound := by
  unfold AtomicMassDatum.qouMass tm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_tm :
    |tm.qouMass - tm.observed| / tm.observed * 100 < tm.pctBound := by
  unfold AtomicMassDatum.qouMass tm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def yb : AtomicMassDatum where
  Z := 70; N := 104; BperA := 8.1280
  observed := 162015.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_yb : |yb.qouMass - yb.observed| < yb.absBound := by
  unfold AtomicMassDatum.qouMass yb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_yb :
    |yb.qouMass - yb.observed| / yb.observed * 100 < yb.pctBound := by
  unfold AtomicMassDatum.qouMass yb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def lu : AtomicMassDatum where
  Z := 71; N := 104; BperA := 8.1165
  observed := 162948.0
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_lu : |lu.qouMass - lu.observed| < lu.absBound := by
  unfold AtomicMassDatum.qouMass lu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_lu :
    |lu.qouMass - lu.observed| / lu.observed * 100 < lu.pctBound := by
  unfold AtomicMassDatum.qouMass lu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def hf : AtomicMassDatum where
  Z := 72; N := 108; BperA := 8.0985
  observed := 167607.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_hf : |hf.qouMass - hf.observed| < hf.absBound := by
  unfold AtomicMassDatum.qouMass hf atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_hf :
    |hf.qouMass - hf.observed| / hf.observed * 100 < hf.pctBound := by
  unfold AtomicMassDatum.qouMass hf atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ta : AtomicMassDatum where
  Z := 73; N := 108; BperA := 8.0870
  observed := 168540.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ta : |ta.qouMass - ta.observed| < ta.absBound := by
  unfold AtomicMassDatum.qouMass ta atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ta :
    |ta.qouMass - ta.observed| / ta.observed * 100 < ta.pctBound := by
  unfold AtomicMassDatum.qouMass ta atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def w : AtomicMassDatum where
  Z := 74; N := 110; BperA := 8.0639
  observed := 171338.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_w : |w.qouMass - w.observed| < w.absBound := by
  unfold AtomicMassDatum.qouMass w atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_w :
    |w.qouMass - w.observed| / w.observed * 100 < w.pctBound := by
  unfold AtomicMassDatum.qouMass w atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def re : AtomicMassDatum where
  Z := 75; N := 112; BperA := 8.0390
  observed := 174136.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_re : |re.qouMass - re.observed| < re.absBound := by
  unfold AtomicMassDatum.qouMass re atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_re :
    |re.qouMass - re.observed| / re.observed * 100 < re.pctBound := by
  unfold AtomicMassDatum.qouMass re atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def os : AtomicMassDatum where
  Z := 76; N := 116; BperA := 8.0194
  observed := 178797.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_os : |os.qouMass - os.observed| < os.absBound := by
  unfold AtomicMassDatum.qouMass os atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_os :
    |os.qouMass - os.observed| / os.observed * 100 < os.pctBound := by
  unfold AtomicMassDatum.qouMass os atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ir : AtomicMassDatum where
  Z := 77; N := 116; BperA := 8.0060
  observed := 179730.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ir : |ir.qouMass - ir.observed| < ir.absBound := by
  unfold AtomicMassDatum.qouMass ir atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ir :
    |ir.qouMass - ir.observed| / ir.observed * 100 < ir.pctBound := by
  unfold AtomicMassDatum.qouMass ir atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def pt : AtomicMassDatum where
  Z := 78; N := 117; BperA := 7.9930
  observed := 181595.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_pt : |pt.qouMass - pt.observed| < pt.absBound := by
  unfold AtomicMassDatum.qouMass pt atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_pt :
    |pt.qouMass - pt.observed| / pt.observed * 100 < pt.pctBound := by
  unfold AtomicMassDatum.qouMass pt atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def au : AtomicMassDatum where
  Z := 79; N := 118; BperA := 7.9759
  observed := 183461.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_au : |au.qouMass - au.observed| < au.absBound := by
  unfold AtomicMassDatum.qouMass au atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_au :
    |au.qouMass - au.observed| / au.observed * 100 < au.pctBound := by
  unfold AtomicMassDatum.qouMass au atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def hg : AtomicMassDatum where
  Z := 80; N := 122; BperA := 7.9530
  observed := 188123.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_hg : |hg.qouMass - hg.observed| < hg.absBound := by
  unfold AtomicMassDatum.qouMass hg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_hg :
    |hg.qouMass - hg.observed| / hg.observed * 100 < hg.pctBound := by
  unfold AtomicMassDatum.qouMass hg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def tl : AtomicMassDatum where
  Z := 81; N := 124; BperA := 7.9370
  observed := 190920.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_tl : |tl.qouMass - tl.observed| < tl.absBound := by
  unfold AtomicMassDatum.qouMass tl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_tl :
    |tl.qouMass - tl.observed| / tl.observed * 100 < tl.pctBound := by
  unfold AtomicMassDatum.qouMass tl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def pb : AtomicMassDatum where
  Z := 82; N := 126; BperA := 7.8675
  observed := 193729.0
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_pb : |pb.qouMass - pb.observed| < pb.absBound := by
  unfold AtomicMassDatum.qouMass pb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_pb :
    |pb.qouMass - pb.observed| / pb.observed * 100 < pb.pctBound := by
  unfold AtomicMassDatum.qouMass pb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def bi : AtomicMassDatum where
  Z := 83; N := 126; BperA := 7.8480
  observed := 194664.0
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_bi : |bi.qouMass - bi.observed| < bi.absBound := by
  unfold AtomicMassDatum.qouMass bi atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_bi :
    |bi.qouMass - bi.observed| / bi.observed * 100 < bi.pctBound := by
  unfold AtomicMassDatum.qouMass bi atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def po : AtomicMassDatum where
  Z := 84; N := 125; BperA := 7.8352
  observed := 194665.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_po : |po.qouMass - po.observed| < po.absBound := by
  unfold AtomicMassDatum.qouMass po atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_po :
    |po.qouMass - po.observed| / po.observed * 100 < po.pctBound := by
  unfold AtomicMassDatum.qouMass po atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def at_ : AtomicMassDatum where
  Z := 85; N := 125; BperA := 7.8147
  observed := 195601.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_at_ : |at_.qouMass - at_.observed| < at_.absBound := by
  unfold AtomicMassDatum.qouMass at_ atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_at_ :
    |at_.qouMass - at_.observed| / at_.observed * 100 < at_.pctBound := by
  unfold AtomicMassDatum.qouMass at_ atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def rn : AtomicMassDatum where
  Z := 86; N := 136; BperA := 7.7227
  observed := 206801.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_rn : |rn.qouMass - rn.observed| < rn.absBound := by
  unfold AtomicMassDatum.qouMass rn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_rn :
    |rn.qouMass - rn.observed| / rn.observed * 100 < rn.pctBound := by
  unfold AtomicMassDatum.qouMass rn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def fr : AtomicMassDatum where
  Z := 87; N := 136; BperA := 7.7095
  observed := 207735.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_fr : |fr.qouMass - fr.observed| < fr.absBound := by
  unfold AtomicMassDatum.qouMass fr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_fr :
    |fr.qouMass - fr.observed| / fr.observed * 100 < fr.pctBound := by
  unfold AtomicMassDatum.qouMass fr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ra : AtomicMassDatum where
  Z := 88; N := 138; BperA := 7.6620
  observed := 210541.3
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ra : |ra.qouMass - ra.observed| < ra.absBound := by
  unfold AtomicMassDatum.qouMass ra atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ra :
    |ra.qouMass - ra.observed| / ra.observed * 100 < ra.pctBound := by
  unfold AtomicMassDatum.qouMass ra atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def ac : AtomicMassDatum where
  Z := 89; N := 138; BperA := 7.6510
  observed := 211474.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ac : |ac.qouMass - ac.observed| < ac.absBound := by
  unfold AtomicMassDatum.qouMass ac atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ac :
    |ac.qouMass - ac.observed| / ac.observed * 100 < ac.pctBound := by
  unfold AtomicMassDatum.qouMass ac atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def th : AtomicMassDatum where
  Z := 90; N := 142; BperA := 7.6150
  observed := 216142.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_th : |th.qouMass - th.observed| < th.absBound := by
  unfold AtomicMassDatum.qouMass th atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_th :
    |th.qouMass - th.observed| / th.observed * 100 < th.pctBound := by
  unfold AtomicMassDatum.qouMass th atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def pa : AtomicMassDatum where
  Z := 91; N := 140; BperA := 7.6138
  observed := 215209.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_pa : |pa.qouMass - pa.observed| < pa.absBound := by
  unfold AtomicMassDatum.qouMass pa atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_pa :
    |pa.qouMass - pa.observed| / pa.observed * 100 < pa.pctBound := by
  unfold AtomicMassDatum.qouMass pa atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
noncomputable def u : AtomicMassDatum where
  Z := 92; N := 146; BperA := 7.5701
  observed := 221742.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_u : |u.qouMass - u.observed| < u.absBound := by
  unfold AtomicMassDatum.qouMass u atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_u :
    |u.qouMass - u.observed| / u.observed * 100 < u.pctBound := by
  unfold AtomicMassDatum.qouMass u atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def np : AtomicMassDatum where
  Z := 93; N := 144; BperA := 7.5753
  observed := 220808.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_np : |np.qouMass - np.observed| < np.absBound := by
  unfold AtomicMassDatum.qouMass np atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_np :
    |np.qouMass - np.observed| / np.observed * 100 < np.pctBound := by
  unfold AtomicMassDatum.qouMass np atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def pu : AtomicMassDatum where
  Z := 94; N := 150; BperA := 7.5242
  observed := 227344.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_pu : |pu.qouMass - pu.observed| < pu.absBound := by
  unfold AtomicMassDatum.qouMass pu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_pu :
    |pu.qouMass - pu.observed| / pu.observed * 100 < pu.pctBound := by
  unfold AtomicMassDatum.qouMass pu atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def am : AtomicMassDatum where
  Z := 95; N := 148; BperA := 7.5249
  observed := 226411.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_am : |am.qouMass - am.observed| < am.absBound := by
  unfold AtomicMassDatum.qouMass am atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_am :
    |am.qouMass - am.observed| / am.observed * 100 < am.pctBound := by
  unfold AtomicMassDatum.qouMass am atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def cm : AtomicMassDatum where
  Z := 96; N := 151; BperA := 7.4988
  observed := 230145.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cm : |cm.qouMass - cm.observed| < cm.absBound := by
  unfold AtomicMassDatum.qouMass cm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cm :
    |cm.qouMass - cm.observed| / cm.observed * 100 < cm.pctBound := by
  unfold AtomicMassDatum.qouMass cm atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def bk : AtomicMassDatum where
  Z := 97; N := 150; BperA := 7.4980
  observed := 230144.8
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_bk : |bk.qouMass - bk.observed| < bk.absBound := by
  unfold AtomicMassDatum.qouMass bk atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_bk :
    |bk.qouMass - bk.observed| / bk.observed * 100 < bk.pctBound := by
  unfold AtomicMassDatum.qouMass bk atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def cf : AtomicMassDatum where
  Z := 98; N := 153; BperA := 7.4688
  observed := 233879.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cf : |cf.qouMass - cf.observed| < cf.absBound := by
  unfold AtomicMassDatum.qouMass cf atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cf :
    |cf.qouMass - cf.observed| / cf.observed * 100 < cf.pctBound := by
  unfold AtomicMassDatum.qouMass cf atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def es : AtomicMassDatum where
  Z := 99; N := 153; BperA := 7.4496
  observed := 234815.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_es : |es.qouMass - es.observed| < es.absBound := by
  unfold AtomicMassDatum.qouMass es atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_es :
    |es.qouMass - es.observed| / es.observed * 100 < es.pctBound := by
  unfold AtomicMassDatum.qouMass es atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def fm : AtomicMassDatum where
  Z := 100; N := 157; BperA := 7.4197
  observed := 239483.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_fm : |fm.qouMass - fm.observed| < fm.absBound := by
  unfold AtomicMassDatum.qouMass fm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_fm :
    |fm.qouMass - fm.observed| / fm.observed * 100 < fm.pctBound := by
  unfold AtomicMassDatum.qouMass fm atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def md : AtomicMassDatum where
  Z := 101; N := 157; BperA := 7.4039
  observed := 240418.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_md : |md.qouMass - md.observed| < md.absBound := by
  unfold AtomicMassDatum.qouMass md atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_md :
    |md.qouMass - md.observed| / md.observed * 100 < md.pctBound := by
  unfold AtomicMassDatum.qouMass md atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def no_ : AtomicMassDatum where
  Z := 102; N := 157; BperA := 7.3900
  observed := 241353.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_no_ : |no_.qouMass - no_.observed| < no_.absBound := by
  unfold AtomicMassDatum.qouMass no_ atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_no_ :
    |no_.qouMass - no_.observed| / no_.observed * 100 < no_.pctBound := by
  unfold AtomicMassDatum.qouMass no_ atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def lr : AtomicMassDatum where
  Z := 103; N := 163; BperA := 7.3540
  observed := 247887.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_lr : |lr.qouMass - lr.observed| < lr.absBound := by
  unfold AtomicMassDatum.qouMass lr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_lr :
    |lr.qouMass - lr.observed| / lr.observed * 100 < lr.pctBound := by
  unfold AtomicMassDatum.qouMass lr atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def rf : AtomicMassDatum where
  Z := 104; N := 163; BperA := 7.3380
  observed := 248823.4
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_rf : |rf.qouMass - rf.observed| < rf.absBound := by
  unfold AtomicMassDatum.qouMass rf atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_rf :
    |rf.qouMass - rf.observed| / rf.observed * 100 < rf.pctBound := by
  unfold AtomicMassDatum.qouMass rf atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def db : AtomicMassDatum where
  Z := 105; N := 163; BperA := 7.3200
  observed := 249759.6
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_db : |db.qouMass - db.observed| < db.absBound := by
  unfold AtomicMassDatum.qouMass db atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_db :
    |db.qouMass - db.observed| / db.observed * 100 < db.pctBound := by
  unfold AtomicMassDatum.qouMass db atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def sg : AtomicMassDatum where
  Z := 106; N := 163; BperA := 7.3020
  observed := 250695.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_sg : |sg.qouMass - sg.observed| < sg.absBound := by
  unfold AtomicMassDatum.qouMass sg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_sg :
    |sg.qouMass - sg.observed| / sg.observed * 100 < sg.pctBound := by
  unfold AtomicMassDatum.qouMass sg atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def bh : AtomicMassDatum where
  Z := 107; N := 163; BperA := 7.2830
  observed := 251632.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_bh : |bh.qouMass - bh.observed| < bh.absBound := by
  unfold AtomicMassDatum.qouMass bh atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_bh :
    |bh.qouMass - bh.observed| / bh.observed * 100 < bh.pctBound := by
  unfold AtomicMassDatum.qouMass bh atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def hs : AtomicMassDatum where
  Z := 108; N := 169; BperA := 7.2560
  observed := 258165.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_hs : |hs.qouMass - hs.observed| < hs.absBound := by
  unfold AtomicMassDatum.qouMass hs atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_hs :
    |hs.qouMass - hs.observed| / hs.observed * 100 < hs.pctBound := by
  unfold AtomicMassDatum.qouMass hs atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def mt : AtomicMassDatum where
  Z := 109; N := 169; BperA := 7.2370
  observed := 259102.0
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_mt : |mt.qouMass - mt.observed| < mt.absBound := by
  unfold AtomicMassDatum.qouMass mt atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_mt :
    |mt.qouMass - mt.observed| / mt.observed * 100 < mt.pctBound := by
  unfold AtomicMassDatum.qouMass mt atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def ds : AtomicMassDatum where
  Z := 110; N := 171; BperA := 7.2110
  observed := 261905.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ds : |ds.qouMass - ds.observed| < ds.absBound := by
  unfold AtomicMassDatum.qouMass ds atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ds :
    |ds.qouMass - ds.observed| / ds.observed * 100 < ds.pctBound := by
  unfold AtomicMassDatum.qouMass ds atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def rg : AtomicMassDatum where
  Z := 111; N := 171; BperA := 7.1910
  observed := 262842.7
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_rg : |rg.qouMass - rg.observed| < rg.absBound := by
  unfold AtomicMassDatum.qouMass rg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_rg :
    |rg.qouMass - rg.observed| / rg.observed * 100 < rg.pctBound := by
  unfold AtomicMassDatum.qouMass rg atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def cn : AtomicMassDatum where
  Z := 112; N := 173; BperA := 7.1650
  observed := 265646.5
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_cn : |cn.qouMass - cn.observed| < cn.absBound := by
  unfold AtomicMassDatum.qouMass cn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_cn :
    |cn.qouMass - cn.observed| / cn.observed * 100 < cn.pctBound := by
  unfold AtomicMassDatum.qouMass cn atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def nh : AtomicMassDatum where
  Z := 113; N := 173; BperA := 7.1440
  observed := 266584.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_nh : |nh.qouMass - nh.observed| < nh.absBound := by
  unfold AtomicMassDatum.qouMass nh atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_nh :
    |nh.qouMass - nh.observed| / nh.observed * 100 < nh.pctBound := by
  unfold AtomicMassDatum.qouMass nh atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def fl : AtomicMassDatum where
  Z := 114; N := 175; BperA := 7.1180
  observed := 269388.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_fl : |fl.qouMass - fl.observed| < fl.absBound := by
  unfold AtomicMassDatum.qouMass fl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_fl :
    |fl.qouMass - fl.observed| / fl.observed * 100 < fl.pctBound := by
  unfold AtomicMassDatum.qouMass fl atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def mc : AtomicMassDatum where
  Z := 115; N := 175; BperA := 7.0960
  observed := 270326.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_mc : |mc.qouMass - mc.observed| < mc.absBound := by
  unfold AtomicMassDatum.qouMass mc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_mc :
    |mc.qouMass - mc.observed| / mc.observed * 100 < mc.pctBound := by
  unfold AtomicMassDatum.qouMass mc atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def lv : AtomicMassDatum where
  Z := 116; N := 177; BperA := 7.0200
  observed := 273145.1
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_lv : |lv.qouMass - lv.observed| < lv.absBound := by
  unfold AtomicMassDatum.qouMass lv atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_lv :
    |lv.qouMass - lv.observed| / lv.observed * 100 < lv.pctBound := by
  unfold AtomicMassDatum.qouMass lv atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def ts : AtomicMassDatum where
  Z := 117; N := 177; BperA := 6.9960
  observed := 274083.9
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_ts : |ts.qouMass - ts.observed| < ts.absBound := by
  unfold AtomicMassDatum.qouMass ts atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_ts :
    |ts.qouMass - ts.observed| / ts.observed * 100 < ts.pctBound := by
  unfold AtomicMassDatum.qouMass ts atomic_mass m_p m_n m_e
  norm_num

-- [Synthetic element — reactor/accelerator produced]
-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
noncomputable def og : AtomicMassDatum where
  Z := 118; N := 176; BperA := 6.9720
  observed := 274090.2
  absBound := 0.1
  pctBound := 0.01

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem deviation_og : |og.qouMass - og.observed| < og.absBound := by
  unfold AtomicMassDatum.qouMass og atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
theorem pct_deviation_og :
    |og.qouMass - og.observed| / og.observed * 100 < og.pctBound := by
  unfold AtomicMassDatum.qouMass og atomic_mass m_p m_n m_e
  norm_num

end QOU.AtomicMass