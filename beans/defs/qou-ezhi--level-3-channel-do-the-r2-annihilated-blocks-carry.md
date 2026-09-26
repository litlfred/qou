---
# qou-ezhi
title: 'Level-3 channel: do the r=2-annihilated blocks carry a colour observable?'
status: completed
type: task
priority: normal
created_at: 2026-09-02T20:52:19Z
updated_at: 2026-09-02T21:01:13Z
---


RESOLVED 2026-09-01 -- computations/probes/level_three_colour_channel_probe.py,
6/6. YES, they carry one -- and the substrate FAILS it by exactly 2, for the
same reason it fails the nuclear sector.

Runs the named falsification in docs/audits/2026-08-16-wenzl-level-family.md
section 4, recorded there as never executed.

BUILT. z_r = q^(2r-1)(q^2-1)/(q^(2r)-1):
    r=1  1.109978582751   > 1  -- the ONLY level that can unbind
    r=2  0.612688037146   = convention D q^3/(q^2+1)      to 1.15e-41
    r=3  0.449304809090   = the audit's q^5/(q^4+q^2+1)   to 1.15e-41
    r=4  0.369360232236
    r=5  0.322749650471
Since mu = z + d <= z (qou-v3u2), z < 1 forces binding -- so only the abelian
level r=1 could ever unbind anything, and it has room for nothing else.

Weights are U_q(gl_r) quantum dimensions prod [r+j-i]/[h(i,j)], normalised by
sum(y*dim)=1, support exactly l(lambda) <= r. At r=2 they reproduce load_cost's
convention-D weights to 1.14e-8 (its stored-f64 floor). SO THIS CONSTRUCTION
SUBSUMES CONVENTION D AS ITS r=2 MEMBER, and the level-3 channel is now built
rather than hypothesised.

THE COLOUR SINGLET IS EXACTLY ZERO AT r=2:
    r=2:  y(3)=0.505404227  y(2,1)=0.247297887  y(1,1,1)=0.000000000
    r=3:  y(3)=0.378370691  y(2,1)=0.293082487  y(1,1,1)=0.035464334
Three quarks in a baryon are totally antisymmetric in colour, so (1,1,1) IS the
colour singlet. At r=2 its weight is not small, it is exactly zero: THE
SUBSTRATE AS CONFIGURED HAS NO COLOUR SINGLET AT ALL. This is the same fact that
makes H_12 cheap (qou-38i9) -- the blocks that collapse are precisely where
colour would live. The computational win and the absent colour are one
statement.

THE OBSERVABLE, NO FOURTH CALIBRATION. 3 (x) 3 = 3bar + 6, one-gluon-exchange
colour factors <lambda_i.lambda_j>/4:
    3bar (antisymmetric)  C = -2/3   ATTRACTIVE
    6    (symmetric)      C = +1/3   REPULSIVE
    |C_a/C_s| = 2 EXACTLY -- group theory, no error bar, nothing fitted.

Substrate blocks carry q and -1/q at EVERY level, so at d=0:
    L_antisym = +0.104340720320   ATTRACTIVE   CORRECT
    L_sym     = -0.104340720320   REPULSIVE    CORRECT
    |L_a/L_s| =  1.000000000000   QCD wants 2  -- off by exactly 2.0000000000

THE SIGNS COME OUT FREE; THE RATIO IS WRONG BY EXACTLY TWO.

SAME DEGENERACY AS THE NUCLEAR SECTOR. L_antisym + L_sym = 5.74e-42, exactly
zero, because q*(1/q) = 1 i.e. |det T| = 1 -- the Hecke relation T^2 = hT + 1
fixing the eigenvalue product at -1. That is precisely the obstruction qou-o8ww
found capping the nuclear T=0/T=1 ratio at 1 where nature wants 33.7. ONE
MECHANISM CAPS TWO INDEPENDENT SECTORS, quark and nuclear, and the quark version
is the SHARPER test because its target is exact group theory rather than a
measured ratio.

THE FRAMING FIX CANNOT BE UNIVERSAL. From qou-vlrq, e/e_max = (R-1)/(R+1):
    QCD colour  R=2        e = 0.2965907506 = e_max/3  EXACTLY (clean closed form)
    nuclear     R=33.7055  e = 0.8384967429 = 0.942372 e_max
They differ by 2.8271x, so a single universal framing cannot serve both; it
would have to be channel- or scale-dependent, and nothing supplies that.

VERDICT: raising the level does NOT repair the sector. It relabels which blocks
are alive and changes z_r, while leaving the block EIGENVALUES -- and therefore
the whole degeneracy argument -- untouched. Anyone hoping colour would rescue
the nuclear sector should read this as the reason it cannot.

CAVEATS: the colour-factor comparison is an IDENTIFICATION (reading the two
exchange-symmetry blocks as sextet/antitriplet), not a derivation -- no SU(3)
action on strands is constructed and no gluon exchange is modelled. The
attractive/repulsive labels use the |mu|<1 convention from qou-m896; the
L_a + L_s = 0 statement is convention-independent. e = e_max/3 is what a fix
would COST, not a derived value.
