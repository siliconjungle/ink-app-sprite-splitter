# Sprite Splitter

Slice grid sprite sheets, select and preview frames, trim transparent borders and export PNG frames or ZIP packs.

## Install

Requires a running [Ink OS](https://github.com/siliconjungle/ink-os-platform) instance and its `ink-os` CLI. Use Node.js 24 or later for development.

```sh
git clone https://github.com/siliconjungle/ink-app-sprite-splitter.git
cd ink-app-sprite-splitter
npm test
# Select your Ink instance using its CLI connection profile.
ink-os deploy .
```

The CLI deploys committed source from your checkout. Commit any edits before deploying them. No credentials or personal instance configuration belong in this repository.

## Behaviour and limits

Grid layouts only. Inputs are PNG, JPEG or WebP, up to 24 MiB and 16 million pixels. Irregular packed atlases and GIF/video inputs are unsupported.

## Development

`npm run dev` opens a local development server. Preview fixtures are separate from live Ink data.

## License

MIT for app code. Bundled third-party components retain their own licenses and notices.

## Quick preview

Displays supported files without starting the normal editing workflow. Ink OS can select this reader through `desktop.preview.fileTypes`, independently of Open with. Space opens the temporary preview from a selection; Escape or Space dismisses it, and arrow keys browse the supplied item order.
