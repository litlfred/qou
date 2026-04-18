import { definition } from "../../schema/builders";

/**
 * H2O molecular braid: bent triatomic with two O–H single bonds.
 * Two H(1,0) atoms + one O(8,8) atom, 2 shared electron pairs,
 * 2 lone pairs on oxygen — drives the bent ∠HOH ≈ 104.5° geometry.
 */
export default definition({
  label: "def:h2o-molecular-braid",
  title: "Water $\\mathrm{H}_2\\mathrm{O}$ as a molecular braid",
  lean: {
    decl: "QOU.Molecular.H2OBraid",
    validation: "not_checked",
  },
  uses: [
    "def:molecular-braid",
    "def:covalent-bond-shared-trefoil",
    "def:electron-shell-braid-capacity",
    "def:h2-molecular-braid",
    "def:co-molecular-braid",
  ],
  tags: [
    "water",
    "H2O",
    "single-bond",
    "bent",
    "triatomic",
    "lone-pair",
    "molecular-braid",
  ],
});
