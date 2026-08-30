import sys; sys.path.insert(0,'/home/user/qou/computations')
import _path_bridge  # noqa
import mpmath as mp
from _precision import set_compute_dps; set_compute_dps(50)
Q = mp.mpf("1.10998"); H = Q - 1/Q
# Table 1 lists pn as "(doubled)": c=2, d=-h.  The UN-doubled form is c=1, d=-h/2.
det_doubled  = (mp.mpf(2)*H - H)*(-H) - 4          # = -(4 + h^2)
det_undoubled= (mp.mpf(1)*H - H/2)*(-H/2) - 1      # = -(1 + h^2/4)
print(f"  det pn, DOUBLED   (c=2,d=-h)   = {mp.nstr(det_doubled,12)}   "
      f"ln|.| = {mp.nstr(mp.log(abs(det_doubled)),12)}")
print(f"  det pn, UN-DOUBLED(c=1,d=-h/2) = {mp.nstr(det_undoubled,12)}   "
      f"ln|.| = {mp.nstr(mp.log(abs(det_undoubled)),12)}")
K = mp.log(abs(det_undoubled))
print(f"\n  kappa := ln(1 + h^2/4) = {mp.nstr(K,14)}")
R=[("He",2,2,"0.04347"),("Li",3,4,"0.130411"),("Be",4,5,"0.217351"),("B",5,6,"0.326027"),
   ("C",6,6,"0.391232"),("N",7,7,"0.53251"),("O",8,8,"0.695523"),("F",9,10,"0.97808"),
   ("Ne",10,10,"1.086755"),("Na",11,12,"1.434517"),("Mg",12,12,"1.564928"),
   ("Al",13,14,"1.977895"),("Si",14,14,"2.130041"),("P",15,16,"2.608213"),
   ("S",16,16,"2.782094"),("Cl",17,18,"3.325472"),("Ar",18,22,"4.303551"),
   ("K",19,20,"4.129671"),("Ca",20,20,"4.347022")]
print(f"\n{'atom':>5} {'Z*N':>5} {'Phi_2 recorded':>15} {'Z*N*kappa':>15} {'rel err':>11}")
print("-"*58)
worst=mp.mpf(0)
for el,Z,N,p2 in R:
    v=mp.mpf(p2); pred=Z*N*K; e=abs(v-pred)/abs(v); worst=max(worst,e)
    print(f"{el:>5} {Z*N:>5} {p2:>15} {mp.nstr(pred,10):>15} {mp.nstr(e,4):>11}")
print(f"\n  Phi_2 = Z*N*ln(1 + h^2/4)  -- worst relative error {mp.nstr(worst,4)}")
print(f"  (Phi_2 published to 6 decimals; He's own value is 0.04347, 5 digits.)")
print()
print("  => the pn crossing the PRODUCER used is the UN-DOUBLED (1, -h/2),")
print("     not Table 1's doubled (2, -h). Both give chirality ratio -1, so")
print("     Phi_3 is unaffected -- which is why the Phi_3 result held at 19/19.")
print("     (1, -h/2) is exactly symAltRatio_half's hypothesis d = -c*h/2 in")
print("     HeckeLinearReduction.lean.")
