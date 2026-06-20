# Newgale Traffic Monitor - GitHub Codespaces

## How to Use

1. Open this repo in GitHub Codespaces.
2. Wait for the environment to finish building.
3. Run the script:

```bash
python track_traffic.py
```

### Keep it running after closing the tab

Use `tmux`:

```bash
tmux new -s traffic
python track_traffic.py
```

- Detach: Press `Ctrl + B`, then `D`
- Reconnect: `tmux attach -t traffic`

Screenshots are saved in the `screenshots` folder inside the Codespace.
```

Now create the zip.