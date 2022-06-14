from typing import Dict, List

from core.config import Configuration
from core.configservice.base import ConfigService, ConfigServiceMode, ShadowDir

class JoolSIITConfigService(ConfigService):
	name: str = "SIIT-Jool"
	group: str = "Translation"
	directories: List[str] = [ "/etc/jool", ]
	files: List[str] = [ "/etc/jool/jool_siit.conf", ]
	executables: List[str] = [ "/usr/local/bin/jool_siit", ]
	dependencies: List[str] = []
	startup: List[str] = [ "jool_siit file handle /etc/jool/jool_siit.conf", ]
	validate: List[str] = [ "jool_siit global display" ]
	shutdown: List[str] = [ "jool_siit instance remove", ]
	validation_mode: ConfigServiceMode = ConfigServiceMode.BLOCKING
	default_configs: List[Configuration] = []
	modes: Dict[str, Dict[str, str]] = {}
	shadow_directories: List[ShadowDir] = []

	def get_text_template(self, name: str) -> str:
		return """
		{
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

