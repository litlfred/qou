import { definition } from "../../schema/builders";

export default definition({
  label: "def:quaternionic-spectral-resolvents",
  lean: { decl: "QOU.QuaternionicSpectralResolvents" },
  title: "Quaternionic spectral resolvents",
  tags: ["brings-surface", "quaternionic", "spectral"],
  uses: ["def:brings-surface", "rem:jet-shell"],  simulator: { ref: "sim:brings-surface" },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/quaternionic-spectral-resolvents-0.svg", blockIndex: 0, hash: "ab6a8e0c38af" },
    { mime: "image/svg+xml", url: "rendered/quaternionic-spectral-resolvents-1.svg", blockIndex: 1, hash: "2d7f8ea9b4a3" },
  ],

});
