"""
Simple example custom service, used to drive shell commands on a node.
"""
from typing import Tuple

from core.nodes.base import CoreNode
from core.services.coreservices import CoreService, ServiceMode


class JoolNAT64Service(CoreService):
	name: str = "NAT64-Jool"
	group: str = "Translation"
	executables: Tuple[str, ...] = ("/usr/local/bin/jool", )
	dependencies: Tuple[str, ...] = ()
	dirs: Tuple[str, ...] = ("/etc/jool", )
	configs: Tuple[str, ...] = ("/etc/jool/jool.conf", )
	startup: Tuple[str, ...] = ("jool file handle /etc/jool/jool.conf", )
	validate: Tuple[str, ...] = ("jool global display", )
	validation_mode: ServiceMode = ServiceMode.NON_BLOCKING
	shutdown: Tuple[str, ...] = ("jool instance remove", )

	@classmethod
	def generate_config(cls, node: CoreNode, filename: str) -> str:
		return """{
	"framework": "netfilter",
	"instance": "default",

	"global": {
		"pool6": "64:ff9b::/96"
	}
}
"""

