import { Block } from "../../../../../schema/block-schema";

export const WignerSu4AlphaClusterProbe: Block = {
  id: "wigner-su4-alpha-cluster-probe",
  kind: "remark",
  title: "Numerical Probe: SU(4) Alpha-Cluster Capacity and AME Residuals",
  authors: ["Litlfred"],
  date: "2026-06-29",
  tags: ["nuclear-physics", "su4", "alpha-cluster", "audit", "numerical-probe"],
  content: "wigner-su4-alpha-cluster-probe.md",
  uses: ["conj:wigner-su4-from-spin-isospin"]
};
