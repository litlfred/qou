---
# qou-qj21
title: 'PR-Drain-3: Salvage/Port Round 53-114 Existing-Carrier De-Vacuify & BraidKnot/Mass/QBeta Upgrades (51 PRs: 33 in 3A + 18 in 3B, #8142..#8490)'
status: in-progress
type: task
priority: high
created_at: 2026-11-23T20:55:52Z
updated_at: 2026-11-24T01:32:08Z
parent: qou-xip2
---

### Salvage, Rebase & Supersede Workflow (STRICT)
1. Fetch the target branch explicitly: `nice -n 15 git fetch origin <headRefName>` (NEVER bare `git fetch origin`, NEVER `lake build`).
2. Diff against `origin/main` (`git diff origin/main...origin/<headRefName> --stat`):
   - Check every claim against `docs/coordination/owner-rulings.md` (no retired `z_C`, no trefoil primary electron, no `L±` or virtual photons, no float64 in probes, zero fitting).
   - Verify Lean files with single-thread `lean -DautoImplicit=false -s 65536` (`LEAN_NUM_THREADS=1`, `nice -n 15`) and static vacuity/axiom guards (`0 sorryAx`, `0` self-assuming projections).
3. Port clean net-new value into a fresh consolidated PR onto `main`, wait until that consolidating PR is `MERGED`, and then close superseded legacy PRs with:
   `gh pr close <num> --repo litlfred/qou --comment "Consolidated onto main in #<new_pr> (<sha>); closing superseded PR while preserving branch <headRefName> intact."`
4. **CRITICAL BRANCH GUARD:** NEVER pass `--delete-branch` or `-d`! Preserve all remote and local branches intact.

## PR-Drain-3A: Round 75–114 Existing-Carrier De-Vacuify & BraidKnot/Mass Upgrades (#8329..#8490) (`33` PRs)
- **`#8490`** (`feat/round114-li2quniq-magicshell-mup2term-parthook-partcomp-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-pz4m, qou-q7lf, qou-r4w5, qou-rc7b, qou-rj0m
- **`#8488`** (`feat/round113-keyn5six-keyn5val-keystd-lnatconc-lnatopt-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-pg2r, qou-plb2, qou-po7i, qou-prop3b, qou-py7e
- **`#8485`** (`feat/round112-keydef-keyelec-keyfram-keygauge-keymckay-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-ommr, qou-orb6, qou-oyde, qou-p30w, qou-pdgc
- **`#8478`** (`feat/round110-heckelin-hecketypea-hookbeta-hookcompl-hookelast-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-m8zb, qou-mfps, qou-mtx9, qou-n4r9, qou-n7ue
- **`#8476`** (`feat/round109-garnircard-hardwall-heckejmcomm-hecketheta-heckereduction-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-k9yt, qou-kt8o, qou-l1gv, qou-lsib, qou-m8s9
- **`#8473`** (`feat/round108-cyclolval-deltalambda-dressed-edgedecouple-f3eps6-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-jvav, qou-k3er, qou-k448, qou-k54t, qou-k6s6
- **`#8464`** (`feat/round106-cosetmirror-cosetsum-eigenpower-intertwine-murphy-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-grph, qou-gwe9, qou-hrwd, qou-i2ed, qou-ip2a
- **`#8459`** (`feat/round104-binding-bringtrilog-bringwplane-cableshift-centralc2-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add BraidKnot theorems and 80-dps witness for qou-e9pp, qou-eggf, qou-ekgf, qou-f1rs, qou-f4el
- **`#8456`** (`feat/round103-untwisted-ursell-wstd-wedderburn-weighted-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): add Mass theorems and 80-dps witness for qou-ddo8, qou-dgkf, qou-dke6, qou-dld9, qou-drag
- **`#8453`** (`feat/round102-torusinfl-twisted-twobody-tworow-uiccurv-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(mass): Round 102 theorems & 80-dps witness (qou-cdj8, qou-cdjd, qou-cdvx, qou-cm7l, qou-cvx9)
- **`#8450`** (`feat/round101-spurious-complexity-sumsyt-tauqint-threedivk-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(mass): Round 101 theorems & 80-dps witness (qou-bake, qou-baye, qou-bg3w, qou-bi43, qou-bstl)
- **`#8447`** (`feat/round100-saddle-satinvis-satpeak-selrule-selfmutual-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(mass): Round 100 theorems & 80-dps witness (qou-ahsy, qou-ahxm, qou-aj91, qou-akdup, qou-augu)
- **`#8444`** (`feat/round99-qgauge-barparity-fmapprune-pivotal-sl2trace-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(mass): Round 99 theorems & 80-dps witness (qou-a31p, qou-a3lh, qou-ad4t, qou-agvb, qou-ahbz)
- **`#8442`** (`feat/round98-onesep-palindromic-psdtrace-qbetaproxy-confluent-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(mass): Round 98 theorems & 80-dps witness (qou-8vyi, qou-969b, qou-99fk, qou-a0j7, qou-a28x)
- **`#8432`** (`feat/round97-monotone-multbound-ncpart-nonuniform-onebody-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 97 Mass theorems & 80-dps witness (qou-87ms, qou-8fl1, qou-8foz, qou-8jfh, qou-8jjo)
- **`#8428`** (`feat/round96-milnororder-signrep-mirrorsplit-multibond-moebius-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 96 Mass theorems & 80-dps witness (qou-6irj, qou-7jhl, qou-7sin, qou-7tr2, qou-7vh1)
- **`#8426`** (`feat/round95-layout-lowerbound-bondrule-maxcontact-simplex-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 95 Mass theorems & 80-dps witness (qou-5ax1, qou-5ll9, qou-5lsb, qou-63fo, qou-6cm9)
- **`#8424`** (`feat/round94-parity-level-lever1depth2-tauclosed-chainlog-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 94 Mass theorems & 80-dps witness (qou-3x8x, qou-4h26, qou-4kc0, qou-4r5y, qou-4un2)
- **`#8421`** (`feat/round93-strip-kindratio-kohnokz-resolvent-affinenorm-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 93 Mass theorems & 80-dps witness (qou-2wtx, qou-306p, qou-37kk, qou-3ral, qou-3wc5)
- **`#8416`** (`feat/round92-jetmono-jetsign-kzratio-kzunit-kappacorr-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 92 Mass theorems & 80-dps witness (qou-172h, qou-1w90, qou-26f2, qou-2cyi, qou-2cz1)
- **`#8413`** (`feat/round91-diffzero-ggm0-intbond0-idemtr-minpoly3-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 91 theorems & 80-dps witness (qou-03fc, qou-0exp, qou-0gqn, qou-16yn, qou-2szo)
- **`#8410`** (`feat/round90-coldisc-fixlt-comptr-w1ltw3-intzero-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 90 theorems & 80-dps witness (qou-oq5r, qou-prjo, qou-qb9e, qou-qqm4, idt1)
- **`#8408`** (`feat/round89-volgap-transdet-toruscos-expnorm-revmid-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): Round 89 theorems & 80-dps witness (qou-8lxd, qou-dap4, qou-g7f6, qou-hok7, qou-i5d7)
- **`#8401`** (`feat/round87-noalien-mubardiff-multzero-onebodyeq-qbetamul2-43c1`, files=7, lean_mod=5, lean_new=0, py=1 | queue_overlap: `[9191]`): feat(qou): Round 87 theorems & 80-dps witness (qou-ontj, qou-rx2u, qou-sa60, qou-zrbv, qou-v2om)
- **`#8398`** (`feat/round86-irrcubic-resolvent3-dimsum5-tau1-satdiff-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): irreducible cubic linear exclusion, 3-step resolvent, m=5 hook super-doubling, q=1 tau & saturated diff (Round 86)
- **`#8395`** (`feat/round85-ggmstep-idemtrace-twoterm-eigensq-unitmod-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): GGM step recovery, idempotent trace from rank, 2-term order bound, Hecke eigenvalue sq & KZ norm gap (Round 85)
- **`#8393`** (`feat/round84-colourdisc-fixedratio-comptrace-zeroslope-equidcap-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): colour cubic lower bound, 4x fixed colourings, component doubling, zero-slope interface & equidistant cluster cap (Round 84)
- **`#8392`** (`feat/round83-lambdasum-taupos-pairenergy-c1eval-nobranch-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): binding root trace sum, tauAnchor positivity, crossing pair energy, C1 exponent diff & S3 no-root (Round 83)
- **`#8383`** (`feat/round81-deutdress-whitehead0-chain2n-mu3rec-samebond-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): deuteron dressing diff, Whitehead n=0 phase, 2n chain step, mu3 reconstruction & equal-bond invariance (Round 81)
- **`#8351`** (`feat/round78-nzvol-blockself-simplexinv-threestep-meridianshear-43c1`, files=7, lean_mod=5, lean_new=0, py=1): Summary (Round 78 — Nuclear Binding, Mass Theory, Braid/Knot & Archimedean Tower)
- **`#8338`** (`claude/round60-devacuify-6qbv-b9cj`, files=7, lean_mod=5, lean_new=0, py=1 | queue_overlap: `[9191]`): feat(lean): Round 60 de-vacuify qou-085a, qou-mtc9, qou-qspc, qou-ffwk, qou-tmmt
- **`#8337`** (`feat/round76-torusmass-pinchoct-gramsig-motivic-spectrahedral-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean,probes): torus-knot mass ratio non-unit, octahedral glued sum-of-squares, radical y21 closed form, motivic Lefschetz unit, and convention-D spectrahedral collapse (cj212, qou-3q7t, qou-o3ta, qou-u96j, qou-zf9n)
- **`#8329`** (`feat/round75-blocklen-equilateral-bondletter-descent-framing-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean,probes): block-length additivity, R3 equilateral bond bound, bond-letter difference, descent fixed points, and framing split dichotomy (qou-5jqv, qou-ebs6, qou-gba1, qou-fn04, qou-m4fp)

## PR-Drain-3B: Round 53–71 Existing-Carrier De-Vacuify & Mass/QBeta/Hecke Upgrades (#8142..#8300) (`18` PRs)
- **`#8297`** (`feat/round70-tl-threerow-factor-shadow-gluon-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean,probes): TL cleared y3 weight, 3-row Bext(5) & Mayer reconstruct, uniform-bond atom trace, shadow orbit merge count, and 4-crossing gluon PSD (qou-3qrv, qou-3exu, qou-5zl1, qou-56qy, qou-1qsw)
- **`#8293`** (`feat/round69-scale-mobius-adjoint-reduced-trefoil-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean,probes): pure-crossing bond ratio q^4, Mobius shift additivity, GZ 3-knot state totals, reduced prime equivalence, and trefoil Hopf intertwining (qou-v8ct, qou-pzsi, qou-q9ih, qou-qjhc, cj01)
- **`#8285`** (`feat/round68-twobody-deficit-regulator-sdp-milnor-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean,probes): two-body cross difference, surface bond deficit, BFHW-MS regulator shift, O3' SDP additivity, and Milnor Hankel defect (qou-tbpl, qou-v0yw, qou-uh5f, qou-sv7h, qou-ix0x)
- **`#8279`** (`feat/round67-diproton-coordination-markov-cut-parity-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean,probes): diproton classical q=1 values, Ursell reconstruct, Markov bridge-pair product, mirror cut invariance, and parity-slope Cayley (qou-ales, qou-edt7, qou-gr3t, qou-qve5, qou-vwu3)
- **`#8257`** (`feat/round63-markov-transfer-fixedpoint-jones-gz-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): H3 Markov trace additivity, transfer chain concatenation, Burnside fixed colourings, convention-D loop gap, and GZ rank shift (qou-46ab, qou-48is, qou-8uxw, qou-98g5, qou-ckbv)
- **`#8255`** (`feat/round62-a4-b3agg-berezinian-wlambda-crossing-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean): A=4 interface operator, b3Agg secant threshold, Berezinian A=3 inverse, W_lambda mixing fractions, and crossing quadratic proton pairs (qou-0qmr, qou-2ss0, qou-6r6d, qou-9nq9, qou-dhsn)
- **`#8238`** (`feat/round60-interface-kappa-geodesic-em-connsum-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): interface scalar, deuteron kappa, geodesic inter, E-M midpoint & connected-sum closure (qou-5d6k, qou-6he8, qou-r111, qou-shrp, qou-zhep)
- **`#8231`** (`feat/round59-hyperbolic-planck-oneloop-qint-dilog-43c1`, files=7, lean_mod=5, lean_new=0, py=1 | queue_overlap: `[9207]`): feat(qou): hyperbolic volume, Planck step, 1-loop det, q-int & dilog theorems (qou-6eik, qou-adwi, qou-fl4t, qou-ltal, qou-mlbg)
- **`#8222`** (`feat/round58-keystone-writhe-ramified-stokes-ladder-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): round 58 keystone LR fold, writhe power/anchor shift, ramified shift, q->0 invariants, and ladder deficit (qou-2v7k, qou-6nd0, qou-p6m1, qou-qnnq, qou-wxhi)
- **`#8213`** (`feat/round57-recurrence-interface-magnus-meridian-fivetwo-43c1`, files=7, lean_mod=5, lean_new=0, py=1 | queue_overlap: `[9189]`): feat(qou): round 57 recurrence depth, separable interface, Magnus Leibniz, meridian winding, and 5_2 cyclotomic transport (qou-i5yp, qou-o43i, qou-o6ov, qou-offl, qou-trns)
- **`#8207`** (`feat/round56-layout-geomtail-neutrality-slq2-kz-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): formalize layout colour mismatch, geometric tail sweep, neutrality sign change, SLq2 odd-A exclusion, and KZ inverse (qou-0c19, qou-0gbx, qou-17mq, qou-768r, qou-d0qq)
- **`#8202`** (`feat/round55-he4-hadamard-deuteron-plancherel-mirror-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(qou): formalize He-4 share, Route D product closure, deuteron sign invariance, normalizer triage, and mirror-pair defect (qou-85wn, qou-blla, qou-e5jf, qou-uk8o, qou-vudb)
- **`#8198`** (`feat/round54-boxcontent-ward-nv-interface-binding-43c1`, files=7, lean_mod=5, lean_new=0, py=1): feat(lean,qbeta,hecke): formalize qou-59x9, qou-58r5, qou-5lib, qou-7zob, qou-2pnv + 80-dps witness
- **`#8179`** (`feat/qou-10v9-tail-d6-lp-dual-altchar-vlevel-2026-11-16`, files=6, lean_mod=4, lean_new=0, py=1): feat(lean,probes): depth-1 nu_{n-1} onset, LP dual certificate reduction, 4-letter altChar sandwich, and v-level 1/g=5g(1+x/5) (qou-1a69, qou-ec5z, qou-k4f8, qou-efqx, qou-xajh)
- **`#8171`** (`feat/qou-wp3h-delta-mrel-n04i-ncgk-3fqa-2026-11-16`, files=4, lean_mod=2, lean_new=0, py=1): feat(lean,probes): delta-split role decoupling, relational m_e factorization, and 2D Yekutieli / 4-Phi_q holonomy (qou-nbx7, qou-mrel, qou-n04i, qou-ncgk, qou-3fqa)
- **`#8164`** (`feat/qou-wp3h-na-stokes-bar-parity-bond21-2026-11-16`, files=5, lean_mod=1, lean_new=0, py=1): feat(lean,probes,prose): NA-Stokes bar-parity split, Yekutieli (2,1) bond projection, and relational-mass prose (qou-ch8w, qou-quv8, qou-yczy, qou-h5aw, qou-n4u6)
- **`#8160`** (`feat/qou-wp3h-rtxm-8gzz-0w42-tknh-bhrx-2026-11-16`, files=4, lean_mod=4, lean_new=0, py=0 | queue_overlap: `[9192]`): feat(lean): close 8gzz, qou-0w42, qou-tknh, qou-bhrx (0 sorry)
- **`#8142`** (`fix/qou-wxhi-2002-q2oa-zuva-6gf9`, files=4, lean_mod=2, lean_new=0, py=1): fix(wxhi,2002): formalize qou-q2oa/zuva Wedderburn vs ladder phase discrepancy and add qou-6gf9 Habiro Laurent probe

Full 51-PR classification ledger committed at be31f5738bf (docs/audits/2026-11-23-backlog-drain-batch3-ledger.md): 2 superseded (#8160, #8338), 3 full-PR merge candidates (#8351, #8392, #8393), 9 Lean-only salvage candidates, 37 stale/failing.
