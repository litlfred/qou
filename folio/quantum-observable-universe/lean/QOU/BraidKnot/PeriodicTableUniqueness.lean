import QOU.BraidKnot.NucleusEmptySDPUniqueness

/-!
# QOU.BraidKnot.PeriodicTableUniqueness — full periodic table coverage

Element-level wrappers for `NucleusEmptySDPUniqueness` covering all
118 elements of the periodic table (H through Og), using the
**AME2020 reference isotope per element** as listed in
`AtomicMass.lean`. Each wrapper specialises the parameterised
`nucleus_uniqueness_closed` at `n = 3A` where `A` is the element's
mass number per AME2020.

## Coverage matrix

For every element with `(Z, N, A)` per AtomicMass.lean:
- `<element>_emptySDP : SDPPrimal (heckeDim (3*A)) ℝ Empty`
- `<element>_uniqueness_closed` — sorry-free, axiom-free

## What this generalises

The existing per-isotope files (`AppliedHelium3Uniqueness.lean`,
`AppliedDeuteronUniqueness.lean`, etc.) cover QOU-tracked specific
isotopes (²H, ³H, ³He, ⁴He, ⁶Li, ⁹Be, ¹¹B, ¹²C, ¹⁴N, ¹⁶O). This
file extends coverage to the full periodic table at the
AME2020-reference-isotope level. Together they cover both:
- QOU's R5-full-solver-tracked specific isotopes (per-isotope files)
- Every chemical element's reference isotope (this file)

## Naming convention

`<element_lowercase>_<theorem_name>` where `element_lowercase` is the
short lowercase symbol used in AtomicMass.lean. For H/He this
collides with the per-isotope notation (e.g. `helium3_emptySDP` vs
`he_emptySDP`); they refer to different isotopes (³He vs ⁴He) and
the per-isotope versions take precedence in disambiguation.

## What this does NOT cover

Same caveat as `NucleusEmptySDPUniqueness`: this is the
**abstract-framework demonstration** at the empty-SDP level. The
real per-element / per-isotope SDP (with multi-term cost from the
mass formula and non-empty constraints) is element-specific
substantive open work.

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (parameterised proof)
- `QOU.AtomicMass` (element data source — AME2020)
-/

namespace QOU.BraidKnot


/-- Hydrogen (Z=1, N=0, A=1). -/
abbrev h_emptySDP := nucleusEmptySDP 3
/-- Hydrogen sorry-free uniqueness. -/
abbrev h_uniqueness_closed := @nucleus_uniqueness_closed 3

/-- Helium (Z=2, N=2, A=4). -/
abbrev he_emptySDP := nucleusEmptySDP 12
/-- Helium sorry-free uniqueness. -/
abbrev he_uniqueness_closed := @nucleus_uniqueness_closed 12

/-- Lithium (Z=3, N=4, A=7). -/
abbrev li_emptySDP := nucleusEmptySDP 21
/-- Lithium sorry-free uniqueness. -/
abbrev li_uniqueness_closed := @nucleus_uniqueness_closed 21

/-- Beryllium (Z=4, N=5, A=9). -/
abbrev be_emptySDP := nucleusEmptySDP 27
/-- Beryllium sorry-free uniqueness. -/
abbrev be_uniqueness_closed := @nucleus_uniqueness_closed 27

/-- Boron (Z=5, N=6, A=11). -/
abbrev b_el_emptySDP := nucleusEmptySDP 33
/-- Boron sorry-free uniqueness. -/
abbrev b_el_uniqueness_closed := @nucleus_uniqueness_closed 33

/-- Carbon (Z=6, N=6, A=12). -/
abbrev c_emptySDP := nucleusEmptySDP 36
/-- Carbon sorry-free uniqueness. -/
abbrev c_uniqueness_closed := @nucleus_uniqueness_closed 36

/-- Nitrogen (Z=7, N=7, A=14). -/
abbrev n_el_emptySDP := nucleusEmptySDP 42
/-- Nitrogen sorry-free uniqueness. -/
abbrev n_el_uniqueness_closed := @nucleus_uniqueness_closed 42

/-- Oxygen (Z=8, N=8, A=16). -/
abbrev o_emptySDP := nucleusEmptySDP 48
/-- Oxygen sorry-free uniqueness. -/
abbrev o_uniqueness_closed := @nucleus_uniqueness_closed 48

/-- Fluorine (Z=9, N=10, A=19). -/
abbrev f_emptySDP := nucleusEmptySDP 57
/-- Fluorine sorry-free uniqueness. -/
abbrev f_uniqueness_closed := @nucleus_uniqueness_closed 57

/-- Neon (Z=10, N=10, A=20). -/
abbrev ne_emptySDP := nucleusEmptySDP 60
/-- Neon sorry-free uniqueness. -/
abbrev ne_uniqueness_closed := @nucleus_uniqueness_closed 60

/-- Sodium (Z=11, N=12, A=23). -/
abbrev na_emptySDP := nucleusEmptySDP 69
/-- Sodium sorry-free uniqueness. -/
abbrev na_uniqueness_closed := @nucleus_uniqueness_closed 69

/-- Magnesium (Z=12, N=12, A=24). -/
abbrev mg_emptySDP := nucleusEmptySDP 72
/-- Magnesium sorry-free uniqueness. -/
abbrev mg_uniqueness_closed := @nucleus_uniqueness_closed 72

/-- Aluminium (Z=13, N=14, A=27). -/
abbrev al_emptySDP := nucleusEmptySDP 81
/-- Aluminium sorry-free uniqueness. -/
abbrev al_uniqueness_closed := @nucleus_uniqueness_closed 81

/-- Silicon (Z=14, N=14, A=28). -/
abbrev si_emptySDP := nucleusEmptySDP 84
/-- Silicon sorry-free uniqueness. -/
abbrev si_uniqueness_closed := @nucleus_uniqueness_closed 84

/-- Phosphorus (Z=15, N=16, A=31). -/
abbrev p_el_emptySDP := nucleusEmptySDP 93
/-- Phosphorus sorry-free uniqueness. -/
abbrev p_el_uniqueness_closed := @nucleus_uniqueness_closed 93

/-- Sulfur (Z=16, N=16, A=32). -/
abbrev s_el_emptySDP := nucleusEmptySDP 96
/-- Sulfur sorry-free uniqueness. -/
abbrev s_el_uniqueness_closed := @nucleus_uniqueness_closed 96

/-- Chlorine (Z=17, N=18, A=35). -/
abbrev cl_emptySDP := nucleusEmptySDP 105
/-- Chlorine sorry-free uniqueness. -/
abbrev cl_uniqueness_closed := @nucleus_uniqueness_closed 105

/-- Argon (Z=18, N=22, A=40). -/
abbrev ar_emptySDP := nucleusEmptySDP 120
/-- Argon sorry-free uniqueness. -/
abbrev ar_uniqueness_closed := @nucleus_uniqueness_closed 120

/-- Potassium (Z=19, N=20, A=39). -/
abbrev k_el_emptySDP := nucleusEmptySDP 117
/-- Potassium sorry-free uniqueness. -/
abbrev k_el_uniqueness_closed := @nucleus_uniqueness_closed 117

/-- Calcium (Z=20, N=20, A=40). -/
abbrev ca_emptySDP := nucleusEmptySDP 120
/-- Calcium sorry-free uniqueness. -/
abbrev ca_uniqueness_closed := @nucleus_uniqueness_closed 120

/-- Scandium (Z=21, N=24, A=45). -/
abbrev sc_emptySDP := nucleusEmptySDP 135
/-- Scandium sorry-free uniqueness. -/
abbrev sc_uniqueness_closed := @nucleus_uniqueness_closed 135

/-- Titanium (Z=22, N=26, A=48). -/
abbrev ti_emptySDP := nucleusEmptySDP 144
/-- Titanium sorry-free uniqueness. -/
abbrev ti_uniqueness_closed := @nucleus_uniqueness_closed 144

/-- Vanadium (Z=23, N=28, A=51). -/
abbrev v_el_emptySDP := nucleusEmptySDP 153
/-- Vanadium sorry-free uniqueness. -/
abbrev v_el_uniqueness_closed := @nucleus_uniqueness_closed 153

/-- Chromium (Z=24, N=28, A=52). -/
abbrev cr_emptySDP := nucleusEmptySDP 156
/-- Chromium sorry-free uniqueness. -/
abbrev cr_uniqueness_closed := @nucleus_uniqueness_closed 156

/-- Manganese (Z=25, N=30, A=55). -/
abbrev mn_emptySDP := nucleusEmptySDP 165
/-- Manganese sorry-free uniqueness. -/
abbrev mn_uniqueness_closed := @nucleus_uniqueness_closed 165

/-- Iron (Z=26, N=30, A=56). -/
abbrev fe_emptySDP := nucleusEmptySDP 168
/-- Iron sorry-free uniqueness. -/
abbrev fe_uniqueness_closed := @nucleus_uniqueness_closed 168

/-- Cobalt (Z=27, N=32, A=59). -/
abbrev co_emptySDP := nucleusEmptySDP 177
/-- Cobalt sorry-free uniqueness. -/
abbrev co_uniqueness_closed := @nucleus_uniqueness_closed 177

/-- Nickel (Z=28, N=30, A=58). -/
abbrev ni_emptySDP := nucleusEmptySDP 174
/-- Nickel sorry-free uniqueness. -/
abbrev ni_uniqueness_closed := @nucleus_uniqueness_closed 174

/-- Copper (Z=29, N=34, A=63). -/
abbrev cu_emptySDP := nucleusEmptySDP 189
/-- Copper sorry-free uniqueness. -/
abbrev cu_uniqueness_closed := @nucleus_uniqueness_closed 189

/-- Zinc (Z=30, N=34, A=64). -/
abbrev zn_emptySDP := nucleusEmptySDP 192
/-- Zinc sorry-free uniqueness. -/
abbrev zn_uniqueness_closed := @nucleus_uniqueness_closed 192

/-- Gallium (Z=31, N=38, A=69). -/
abbrev ga_emptySDP := nucleusEmptySDP 207
/-- Gallium sorry-free uniqueness. -/
abbrev ga_uniqueness_closed := @nucleus_uniqueness_closed 207

/-- Germanium (Z=32, N=42, A=74). -/
abbrev ge_emptySDP := nucleusEmptySDP 222
/-- Germanium sorry-free uniqueness. -/
abbrev ge_uniqueness_closed := @nucleus_uniqueness_closed 222

/-- Arsenic (Z=33, N=42, A=75). -/
abbrev as_el_emptySDP := nucleusEmptySDP 225
/-- Arsenic sorry-free uniqueness. -/
abbrev as_el_uniqueness_closed := @nucleus_uniqueness_closed 225

/-- Selenium (Z=34, N=46, A=80). -/
abbrev se_emptySDP := nucleusEmptySDP 240
/-- Selenium sorry-free uniqueness. -/
abbrev se_uniqueness_closed := @nucleus_uniqueness_closed 240

/-- Bromine (Z=35, N=44, A=79). -/
abbrev br_emptySDP := nucleusEmptySDP 237
/-- Bromine sorry-free uniqueness. -/
abbrev br_uniqueness_closed := @nucleus_uniqueness_closed 237

/-- Krypton (Z=36, N=48, A=84). -/
abbrev kr_emptySDP := nucleusEmptySDP 252
/-- Krypton sorry-free uniqueness. -/
abbrev kr_uniqueness_closed := @nucleus_uniqueness_closed 252

/-- Rubidium (Z=37, N=48, A=85). -/
abbrev rb_emptySDP := nucleusEmptySDP 255
/-- Rubidium sorry-free uniqueness. -/
abbrev rb_uniqueness_closed := @nucleus_uniqueness_closed 255

/-- Strontium (Z=38, N=50, A=88). -/
abbrev sr_emptySDP := nucleusEmptySDP 264
/-- Strontium sorry-free uniqueness. -/
abbrev sr_uniqueness_closed := @nucleus_uniqueness_closed 264

/-- Yttrium (Z=39, N=50, A=89). -/
abbrev y_el_emptySDP := nucleusEmptySDP 267
/-- Yttrium sorry-free uniqueness. -/
abbrev y_el_uniqueness_closed := @nucleus_uniqueness_closed 267

/-- Zirconium (Z=40, N=50, A=90). -/
abbrev zr_emptySDP := nucleusEmptySDP 270
/-- Zirconium sorry-free uniqueness. -/
abbrev zr_uniqueness_closed := @nucleus_uniqueness_closed 270

/-- Niobium (Z=41, N=52, A=93). -/
abbrev nb_emptySDP := nucleusEmptySDP 279
/-- Niobium sorry-free uniqueness. -/
abbrev nb_uniqueness_closed := @nucleus_uniqueness_closed 279

/-- Molybdenum (Z=42, N=56, A=98). -/
abbrev mo_emptySDP := nucleusEmptySDP 294
/-- Molybdenum sorry-free uniqueness. -/
abbrev mo_uniqueness_closed := @nucleus_uniqueness_closed 294

/-- Technetium (Z=43, N=55, A=98). -/
abbrev tc_emptySDP := nucleusEmptySDP 294
/-- Technetium sorry-free uniqueness. -/
abbrev tc_uniqueness_closed := @nucleus_uniqueness_closed 294

/-- Ruthenium (Z=44, N=58, A=102). -/
abbrev ru_emptySDP := nucleusEmptySDP 306
/-- Ruthenium sorry-free uniqueness. -/
abbrev ru_uniqueness_closed := @nucleus_uniqueness_closed 306

/-- Rhodium (Z=45, N=58, A=103). -/
abbrev rh_emptySDP := nucleusEmptySDP 309
/-- Rhodium sorry-free uniqueness. -/
abbrev rh_uniqueness_closed := @nucleus_uniqueness_closed 309

/-- Palladium (Z=46, N=60, A=106). -/
abbrev pd_emptySDP := nucleusEmptySDP 318
/-- Palladium sorry-free uniqueness. -/
abbrev pd_uniqueness_closed := @nucleus_uniqueness_closed 318

/-- Silver (Z=47, N=60, A=107). -/
abbrev ag_emptySDP := nucleusEmptySDP 321
/-- Silver sorry-free uniqueness. -/
abbrev ag_uniqueness_closed := @nucleus_uniqueness_closed 321

/-- Cadmium (Z=48, N=66, A=114). -/
abbrev cd_emptySDP := nucleusEmptySDP 342
/-- Cadmium sorry-free uniqueness. -/
abbrev cd_uniqueness_closed := @nucleus_uniqueness_closed 342

/-- Indium (Z=49, N=66, A=115). -/
abbrev in_el_emptySDP := nucleusEmptySDP 345
/-- Indium sorry-free uniqueness. -/
abbrev in_el_uniqueness_closed := @nucleus_uniqueness_closed 345

/-- Tin (Z=50, N=70, A=120). -/
abbrev sn_emptySDP := nucleusEmptySDP 360
/-- Tin sorry-free uniqueness. -/
abbrev sn_uniqueness_closed := @nucleus_uniqueness_closed 360

/-- Antimony (Z=51, N=70, A=121). -/
abbrev sb_emptySDP := nucleusEmptySDP 363
/-- Antimony sorry-free uniqueness. -/
abbrev sb_uniqueness_closed := @nucleus_uniqueness_closed 363

/-- Tellurium (Z=52, N=78, A=130). -/
abbrev te_emptySDP := nucleusEmptySDP 390
/-- Tellurium sorry-free uniqueness. -/
abbrev te_uniqueness_closed := @nucleus_uniqueness_closed 390

/-- Iodine (Z=53, N=74, A=127). -/
abbrev i_el_emptySDP := nucleusEmptySDP 381
/-- Iodine sorry-free uniqueness. -/
abbrev i_el_uniqueness_closed := @nucleus_uniqueness_closed 381

/-- Xenon (Z=54, N=78, A=132). -/
abbrev xe_emptySDP := nucleusEmptySDP 396
/-- Xenon sorry-free uniqueness. -/
abbrev xe_uniqueness_closed := @nucleus_uniqueness_closed 396

/-- Caesium (Z=55, N=78, A=133). -/
abbrev cs_emptySDP := nucleusEmptySDP 399
/-- Caesium sorry-free uniqueness. -/
abbrev cs_uniqueness_closed := @nucleus_uniqueness_closed 399

/-- Barium (Z=56, N=82, A=138). -/
abbrev ba_emptySDP := nucleusEmptySDP 414
/-- Barium sorry-free uniqueness. -/
abbrev ba_uniqueness_closed := @nucleus_uniqueness_closed 414

/-- Lanthanum (Z=57, N=82, A=139). -/
abbrev la_emptySDP := nucleusEmptySDP 417
/-- Lanthanum sorry-free uniqueness. -/
abbrev la_uniqueness_closed := @nucleus_uniqueness_closed 417

/-- Cerium (Z=58, N=82, A=140). -/
abbrev ce_emptySDP := nucleusEmptySDP 420
/-- Cerium sorry-free uniqueness. -/
abbrev ce_uniqueness_closed := @nucleus_uniqueness_closed 420

/-- Praseodymium (Z=59, N=82, A=141). -/
abbrev pr_emptySDP := nucleusEmptySDP 423
/-- Praseodymium sorry-free uniqueness. -/
abbrev pr_uniqueness_closed := @nucleus_uniqueness_closed 423

/-- Neodymium (Z=60, N=82, A=142). -/
abbrev nd_emptySDP := nucleusEmptySDP 426
/-- Neodymium sorry-free uniqueness. -/
abbrev nd_uniqueness_closed := @nucleus_uniqueness_closed 426

/-- Promethium (Z=61, N=84, A=145). -/
abbrev pm_emptySDP := nucleusEmptySDP 435
/-- Promethium sorry-free uniqueness. -/
abbrev pm_uniqueness_closed := @nucleus_uniqueness_closed 435

/-- Samarium (Z=62, N=90, A=152). -/
abbrev sm_emptySDP := nucleusEmptySDP 456
/-- Samarium sorry-free uniqueness. -/
abbrev sm_uniqueness_closed := @nucleus_uniqueness_closed 456

/-- Europium (Z=63, N=90, A=153). -/
abbrev eu_emptySDP := nucleusEmptySDP 459
/-- Europium sorry-free uniqueness. -/
abbrev eu_uniqueness_closed := @nucleus_uniqueness_closed 459

/-- Gadolinium (Z=64, N=94, A=158). -/
abbrev gd_emptySDP := nucleusEmptySDP 474
/-- Gadolinium sorry-free uniqueness. -/
abbrev gd_uniqueness_closed := @nucleus_uniqueness_closed 474

/-- Terbium (Z=65, N=94, A=159). -/
abbrev tb_emptySDP := nucleusEmptySDP 477
/-- Terbium sorry-free uniqueness. -/
abbrev tb_uniqueness_closed := @nucleus_uniqueness_closed 477

/-- Dysprosium (Z=66, N=98, A=164). -/
abbrev dy_emptySDP := nucleusEmptySDP 492
/-- Dysprosium sorry-free uniqueness. -/
abbrev dy_uniqueness_closed := @nucleus_uniqueness_closed 492

/-- Holmium (Z=67, N=98, A=165). -/
abbrev ho_emptySDP := nucleusEmptySDP 495
/-- Holmium sorry-free uniqueness. -/
abbrev ho_uniqueness_closed := @nucleus_uniqueness_closed 495

/-- Erbium (Z=68, N=98, A=166). -/
abbrev er_emptySDP := nucleusEmptySDP 498
/-- Erbium sorry-free uniqueness. -/
abbrev er_uniqueness_closed := @nucleus_uniqueness_closed 498

/-- Thulium (Z=69, N=100, A=169). -/
abbrev tm_el_emptySDP := nucleusEmptySDP 507
/-- Thulium sorry-free uniqueness. -/
abbrev tm_el_uniqueness_closed := @nucleus_uniqueness_closed 507

/-- Ytterbium (Z=70, N=104, A=174). -/
abbrev yb_emptySDP := nucleusEmptySDP 522
/-- Ytterbium sorry-free uniqueness. -/
abbrev yb_uniqueness_closed := @nucleus_uniqueness_closed 522

/-- Lutetium (Z=71, N=104, A=175). -/
abbrev lu_emptySDP := nucleusEmptySDP 525
/-- Lutetium sorry-free uniqueness. -/
abbrev lu_uniqueness_closed := @nucleus_uniqueness_closed 525

/-- Hafnium (Z=72, N=108, A=180). -/
abbrev hf_emptySDP := nucleusEmptySDP 540
/-- Hafnium sorry-free uniqueness. -/
abbrev hf_uniqueness_closed := @nucleus_uniqueness_closed 540

/-- Tantalum (Z=73, N=108, A=181). -/
abbrev ta_emptySDP := nucleusEmptySDP 543
/-- Tantalum sorry-free uniqueness. -/
abbrev ta_uniqueness_closed := @nucleus_uniqueness_closed 543

/-- Tungsten (Z=74, N=110, A=184). -/
abbrev w_el_emptySDP := nucleusEmptySDP 552
/-- Tungsten sorry-free uniqueness. -/
abbrev w_el_uniqueness_closed := @nucleus_uniqueness_closed 552

/-- Rhenium (Z=75, N=112, A=187). -/
abbrev re_el_emptySDP := nucleusEmptySDP 561
/-- Rhenium sorry-free uniqueness. -/
abbrev re_el_uniqueness_closed := @nucleus_uniqueness_closed 561

/-- Osmium (Z=76, N=116, A=192). -/
abbrev os_emptySDP := nucleusEmptySDP 576
/-- Osmium sorry-free uniqueness. -/
abbrev os_uniqueness_closed := @nucleus_uniqueness_closed 576

/-- Iridium (Z=77, N=116, A=193). -/
abbrev ir_emptySDP := nucleusEmptySDP 579
/-- Iridium sorry-free uniqueness. -/
abbrev ir_uniqueness_closed := @nucleus_uniqueness_closed 579

/-- Platinum (Z=78, N=117, A=195). -/
abbrev pt_emptySDP := nucleusEmptySDP 585
/-- Platinum sorry-free uniqueness. -/
abbrev pt_uniqueness_closed := @nucleus_uniqueness_closed 585

/-- Gold (Z=79, N=118, A=197). -/
abbrev au_emptySDP := nucleusEmptySDP 591
/-- Gold sorry-free uniqueness. -/
abbrev au_uniqueness_closed := @nucleus_uniqueness_closed 591

/-- Mercury (Z=80, N=122, A=202). -/
abbrev hg_emptySDP := nucleusEmptySDP 606
/-- Mercury sorry-free uniqueness. -/
abbrev hg_uniqueness_closed := @nucleus_uniqueness_closed 606

/-- Thallium (Z=81, N=124, A=205). -/
abbrev tl_emptySDP := nucleusEmptySDP 615
/-- Thallium sorry-free uniqueness. -/
abbrev tl_uniqueness_closed := @nucleus_uniqueness_closed 615

/-- Lead (Z=82, N=126, A=208). -/
abbrev pb_emptySDP := nucleusEmptySDP 624
/-- Lead sorry-free uniqueness. -/
abbrev pb_uniqueness_closed := @nucleus_uniqueness_closed 624

/-- Bismuth (Z=83, N=126, A=209). -/
abbrev bi_emptySDP := nucleusEmptySDP 627
/-- Bismuth sorry-free uniqueness. -/
abbrev bi_uniqueness_closed := @nucleus_uniqueness_closed 627

/-- Polonium (Z=84, N=125, A=209). -/
abbrev po_emptySDP := nucleusEmptySDP 627
/-- Polonium sorry-free uniqueness. -/
abbrev po_uniqueness_closed := @nucleus_uniqueness_closed 627

/-- Astatine (Z=85, N=125, A=210). -/
abbrev at_el_emptySDP := nucleusEmptySDP 630
/-- Astatine sorry-free uniqueness. -/
abbrev at_el_uniqueness_closed := @nucleus_uniqueness_closed 630

/-- Radon (Z=86, N=136, A=222). -/
abbrev rn_emptySDP := nucleusEmptySDP 666
/-- Radon sorry-free uniqueness. -/
abbrev rn_uniqueness_closed := @nucleus_uniqueness_closed 666

/-- Francium (Z=87, N=136, A=223). -/
abbrev fr_el_emptySDP := nucleusEmptySDP 669
/-- Francium sorry-free uniqueness. -/
abbrev fr_el_uniqueness_closed := @nucleus_uniqueness_closed 669

/-- Radium (Z=88, N=138, A=226). -/
abbrev ra_emptySDP := nucleusEmptySDP 678
/-- Radium sorry-free uniqueness. -/
abbrev ra_uniqueness_closed := @nucleus_uniqueness_closed 678

/-- Actinium (Z=89, N=138, A=227). -/
abbrev ac_emptySDP := nucleusEmptySDP 681
/-- Actinium sorry-free uniqueness. -/
abbrev ac_uniqueness_closed := @nucleus_uniqueness_closed 681

/-- Thorium (Z=90, N=142, A=232). -/
abbrev th_emptySDP := nucleusEmptySDP 696
/-- Thorium sorry-free uniqueness. -/
abbrev th_uniqueness_closed := @nucleus_uniqueness_closed 696

/-- Protactinium (Z=91, N=140, A=231). -/
abbrev pa_emptySDP := nucleusEmptySDP 693
/-- Protactinium sorry-free uniqueness. -/
abbrev pa_uniqueness_closed := @nucleus_uniqueness_closed 693

/-- Uranium (Z=92, N=146, A=238). -/
abbrev u_el_emptySDP := nucleusEmptySDP 714
/-- Uranium sorry-free uniqueness. -/
abbrev u_el_uniqueness_closed := @nucleus_uniqueness_closed 714

/-- Neptunium (Z=93, N=144, A=237). -/
abbrev np_emptySDP := nucleusEmptySDP 711
/-- Neptunium sorry-free uniqueness. -/
abbrev np_uniqueness_closed := @nucleus_uniqueness_closed 711

/-- Plutonium (Z=94, N=150, A=244). -/
abbrev pu_emptySDP := nucleusEmptySDP 732
/-- Plutonium sorry-free uniqueness. -/
abbrev pu_uniqueness_closed := @nucleus_uniqueness_closed 732

/-- Americium (Z=95, N=148, A=243). -/
abbrev am_emptySDP := nucleusEmptySDP 729
/-- Americium sorry-free uniqueness. -/
abbrev am_uniqueness_closed := @nucleus_uniqueness_closed 729

/-- Curium (Z=96, N=151, A=247). -/
abbrev cm_emptySDP := nucleusEmptySDP 741
/-- Curium sorry-free uniqueness. -/
abbrev cm_uniqueness_closed := @nucleus_uniqueness_closed 741

/-- Berkelium (Z=97, N=150, A=247). -/
abbrev bk_emptySDP := nucleusEmptySDP 741
/-- Berkelium sorry-free uniqueness. -/
abbrev bk_uniqueness_closed := @nucleus_uniqueness_closed 741

/-- Californium (Z=98, N=153, A=251). -/
abbrev cf_emptySDP := nucleusEmptySDP 753
/-- Californium sorry-free uniqueness. -/
abbrev cf_uniqueness_closed := @nucleus_uniqueness_closed 753

/-- Einsteinium (Z=99, N=153, A=252). -/
abbrev es_emptySDP := nucleusEmptySDP 756
/-- Einsteinium sorry-free uniqueness. -/
abbrev es_uniqueness_closed := @nucleus_uniqueness_closed 756

/-- Fermium (Z=100, N=157, A=257). -/
abbrev fm_emptySDP := nucleusEmptySDP 771
/-- Fermium sorry-free uniqueness. -/
abbrev fm_uniqueness_closed := @nucleus_uniqueness_closed 771

/-- Mendelevium (Z=101, N=157, A=258). -/
abbrev md_el_emptySDP := nucleusEmptySDP 774
/-- Mendelevium sorry-free uniqueness. -/
abbrev md_el_uniqueness_closed := @nucleus_uniqueness_closed 774

/-- Nobelium (Z=102, N=157, A=259). -/
abbrev no_el_emptySDP := nucleusEmptySDP 777
/-- Nobelium sorry-free uniqueness. -/
abbrev no_el_uniqueness_closed := @nucleus_uniqueness_closed 777

/-- Lawrencium (Z=103, N=163, A=266). -/
abbrev lr_emptySDP := nucleusEmptySDP 798
/-- Lawrencium sorry-free uniqueness. -/
abbrev lr_uniqueness_closed := @nucleus_uniqueness_closed 798

/-- Rutherfordium (Z=104, N=163, A=267). -/
abbrev rf_emptySDP := nucleusEmptySDP 801
/-- Rutherfordium sorry-free uniqueness. -/
abbrev rf_uniqueness_closed := @nucleus_uniqueness_closed 801

/-- Dubnium (Z=105, N=163, A=268). -/
abbrev db_emptySDP := nucleusEmptySDP 804
/-- Dubnium sorry-free uniqueness. -/
abbrev db_uniqueness_closed := @nucleus_uniqueness_closed 804

/-- Seaborgium (Z=106, N=163, A=269). -/
abbrev sg_emptySDP := nucleusEmptySDP 807
/-- Seaborgium sorry-free uniqueness. -/
abbrev sg_uniqueness_closed := @nucleus_uniqueness_closed 807

/-- Bohrium (Z=107, N=163, A=270). -/
abbrev bh_emptySDP := nucleusEmptySDP 810
/-- Bohrium sorry-free uniqueness. -/
abbrev bh_uniqueness_closed := @nucleus_uniqueness_closed 810

/-- Hassium (Z=108, N=169, A=277). -/
abbrev hs_emptySDP := nucleusEmptySDP 831
/-- Hassium sorry-free uniqueness. -/
abbrev hs_uniqueness_closed := @nucleus_uniqueness_closed 831

/-- Meitnerium (Z=109, N=169, A=278). -/
abbrev mt_emptySDP := nucleusEmptySDP 834
/-- Meitnerium sorry-free uniqueness. -/
abbrev mt_uniqueness_closed := @nucleus_uniqueness_closed 834

/-- Darmstadtium (Z=110, N=171, A=281). -/
abbrev ds_emptySDP := nucleusEmptySDP 843
/-- Darmstadtium sorry-free uniqueness. -/
abbrev ds_uniqueness_closed := @nucleus_uniqueness_closed 843

/-- Roentgenium (Z=111, N=171, A=282). -/
abbrev rg_emptySDP := nucleusEmptySDP 846
/-- Roentgenium sorry-free uniqueness. -/
abbrev rg_uniqueness_closed := @nucleus_uniqueness_closed 846

/-- Copernicium (Z=112, N=173, A=285). -/
abbrev cn_emptySDP := nucleusEmptySDP 855
/-- Copernicium sorry-free uniqueness. -/
abbrev cn_uniqueness_closed := @nucleus_uniqueness_closed 855

/-- Nihonium (Z=113, N=173, A=286). -/
abbrev nh_emptySDP := nucleusEmptySDP 858
/-- Nihonium sorry-free uniqueness. -/
abbrev nh_uniqueness_closed := @nucleus_uniqueness_closed 858

/-- Flerovium (Z=114, N=175, A=289). -/
abbrev fl_emptySDP := nucleusEmptySDP 867
/-- Flerovium sorry-free uniqueness. -/
abbrev fl_uniqueness_closed := @nucleus_uniqueness_closed 867

/-- Moscovium (Z=115, N=175, A=290). -/
abbrev mc_emptySDP := nucleusEmptySDP 870
/-- Moscovium sorry-free uniqueness. -/
abbrev mc_uniqueness_closed := @nucleus_uniqueness_closed 870

/-- Livermorium (Z=116, N=177, A=293). -/
abbrev lv_emptySDP := nucleusEmptySDP 879
/-- Livermorium sorry-free uniqueness. -/
abbrev lv_uniqueness_closed := @nucleus_uniqueness_closed 879

/-- Tennessine (Z=117, N=177, A=294). -/
abbrev ts_emptySDP := nucleusEmptySDP 882
/-- Tennessine sorry-free uniqueness. -/
abbrev ts_uniqueness_closed := @nucleus_uniqueness_closed 882

/-- Oganesson (Z=118, N=176, A=294). -/
abbrev og_emptySDP := nucleusEmptySDP 882
/-- Oganesson sorry-free uniqueness. -/
abbrev og_uniqueness_closed := @nucleus_uniqueness_closed 882

end QOU.BraidKnot
