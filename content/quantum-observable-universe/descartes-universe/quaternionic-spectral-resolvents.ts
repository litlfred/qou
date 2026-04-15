import { definition } from "../../schema/builders";

export default definition({
  label: "def:quaternionic-spectral-resolvents",
  lean: { decl: "QOU.QuaternionicSpectralResolvents", validation: "not_checked" },
  title: "Quaternionic spectral resolvents",
  tags: ["brings-surface", "quaternionic", "spectral"],
  uses: ["def:brings-surface", "rem:jet-shell"],  simulator: { ref: "sim:brings-surface" },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quaternionic-spectral-resolvents-0.svg", blockIndex: 0, hash: "0b794f189ba7" },
    { mime: "image/svg+xml", url: "rendered/quaternionic-spectral-resolvents-1.svg", blockIndex: 1, hash: "0e5751f7472b" },
  ],

});
