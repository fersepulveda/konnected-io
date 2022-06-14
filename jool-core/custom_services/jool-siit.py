"""
Simple example custom service, used to drive shell commands on a node.
"""
from typing import Tuple

from core.nodes.base import CoreNode
from core.services.coreservices import CoreService, ServiceMode


class JoolSIITService(CoreService):
	name: str = "SIIT-Jool"
	group: str = "Translation"
	executables: Tuple[str, ...] = ("/usr/local/bin/jool_siit", )
	dependencies: Tuple[str, ...] = ()
	dirs: Tuple[str, ...] = ("/etc/jool", )
	configs: Tuple[str, ...] = ("/etc/jool/jool_siit.conf", )
	startup: Tuple[str, ...] = ("jool_siit file handle /etc/jool/jool_siit.conf", )
	validate: Tuple[str, ...] = ("jool_siit global display", )
	validation_mode: ServiceMode = ServiceMode.NON_BLOCKING
	shutdown: Tuple[str, ...] = ("jool_siit instance remove", )

	@classmethod
	def generate_config(cls, node: CoreNode, filename: str) -> str:
		return """{
	"framework": "netfilter",
	"instance": "default",

	"eamt": [
		{
			"ipv6 prefix": "2001::/120",
			"ipv4 prefix": "192.0.2.0/24"
		}, {
			"ipv6 prefix": "4001::/120",
			"ipv4 prefix": "10.0.1.0/24"
		}
	]
}
"""

