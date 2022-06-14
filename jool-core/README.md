# Installation

Install Jool:

```bash
wget https://github.com/NICMx/Jool/releases/download/v4.1.8/jool-dkms_4.1.8-1_all.deb
wget https://github.com/NICMx/Jool/releases/download/v4.1.8/jool-tools_4.1.8-1_amd64.deb
sudo apt install ./jool-dkms_4.1.8-1_all.deb ./jool-tools_4.1.8-1_amd64.deb
```

Install CORE:

```bash
git clone https://github.com/coreemu/core.git
cd core
./setup.sh
source ~/.bashrc
inv install
```

Copy the contents of `custom_config_services/` and `custom_services/` (adjacent to this README) to `~/.coregui`. Directories might or might not already exist:

```bash
mkdir -p ~/.coregui/custom_config_services
mkdir -p ~/.coregui/custom_services
cp custom_config_services/* ~/.coregui/custom_config_services
cp custom_services/* ~/.coregui/custom_services
```

Make sure both directories are referenced by `/etc/core/core.conf`:

```
custom_services_dir        = ~/.coregui/custom_services
custom_config_services_dir = ~/.coregui/custom_config_services
```

Copy the icons to `~/.coregui/icons`:

```bash
cp *.png ~/.coregui/icons
```

Finally, find the `nodes` section in `~/.coregui/config.yaml`, and add Jool's custom nodes to it:

```
nodes:
  - !CustomNode
    image: /home/ahhrk/.coregui/icons/nat64-icon.png
    name: NAT64 (Jool)
    services:
      - NAT64-Jool
      - IPForward
  - !CustomNode
    image: /home/ahhrk/.coregui/icons/siit-icon.png
    name: SIIT (Jool)
    services:
      - IPForward
      - SIIT-Jool
```

Remember to update your username in the `image` paths!

That's it.

# Run

Attach Jool to your kernel:

```bash
sudo modprobe jool
sudo modprobe jool_siit
```

(Do it every time you reboot your system.)

Start or restart the CORE daemon:

```
sudo service core-daemon restart
```

Then start the GUI:

```
core-gui
```

Puedes encontrar los íconos de SIIT y NAT64 en el menú de la izquierda.

Instrucciones viejas:

# Correr NAT64

1. Construye una red poniendo tres nodos y conectando dos cables:

	<laptop> ----------- <NAT64 Jool> --------------- <laptop>
	2001::20         2001::1    10.0.1.1            10.0.1.20

2. Recomiendo que también habilites nombres de redes: `View > Show > Interface names`
3. Play
4. Nota que puedes hacer doble click en el nodo de Jool y ejecutar comandos de Jool comunes y corrientes (como `$ jool g d`).
5. Doble click en el nodo IPv6.
6. `$ ping 64:ff9b::10.0.1.20`
7. Stop
8. Puedes guardar la simulación con `File > Save as <ext>...`

# Correr SIIT

Igual que NAT64, excepto que el nodo traductor tiene que ser un SIIT, y el ping debe verse así:

	ping6 4001::14

Con SIIT también puedes pinguear desde IPv4:

	ping 192.0.2.32

# Otros detalles

- Mientras estés dentro de la simulación (ie. entre Play y Stop), puedes ir a `/tmp/pycore.#####/` y encontrar directorios con las configuraciones de los tres nodos.
- Mientras estés fuera de la simulación, si te vas a la configuración del servicio `SIIT_Jool` o `NAT64_Jool`, puedes hacer modificaciones temporales a la config. Se basa en el formato JSON que tenemos en http://jool.mx/en/config-atomic.html.

