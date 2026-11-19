import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-heat-kernel-peter-weyl",
  label: "rem:q-heat-kernel-computational-fallback",
  title: "Computational fallback at large $k$: $q$-heat kernel and Perron--Frobenius",
  tags: ["computational", "nf-transition", "perron-frobenius", "q-gaussian", "large-k", "hecke"],
  uses: ["prop:q-heat-kernel-peter-weyl"],
  computation: {
    engine: "mpmath",
    script: "computations/binding_heat_kernel_canonical_time_probe.py",
    witness: "computations/binding-heat-kernel-canonical-time.witness.json",
    status: "verified",
  },
});
