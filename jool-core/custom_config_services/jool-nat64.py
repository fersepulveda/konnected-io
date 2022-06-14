from typing import Dict, List

from core.config import Configuration
from core.configservice.base import ConfigService, ConfigServiceMode, ShadowDir

class JoolNAT64ConfigService(ConfigService):
	name: str = "NAT64-Jool"
	group: str = "Translation"
	directories: List[str] = [ "/etc/jool", ]
	files: List[str] = [ "/etc/jool/jool.conf", ]
	executables: List[str] = [ "/usr/local/bin/jool", ]
	dependencies: List[str] = []
	startup: List[str] = [ "jool file handle /etc/jool/jool.conf", ]
	validate: List[str] = [ "jool global display", ]
	shutdown: List[str] = [ "jool instance remove", ]
	validation_mode: ConfigServiceMode = ConfigServiceMode.BLOCKING
	default_configs: List[Configuration] = []
	modes: Dict[str, Dict[str, str]] = {}
	shadow_directories: List[ShadowDir] = []

	def get_text_template(self, name: str) -> str:
		return """
		{
			"framework": "netfilter",
			"instance": "default",

			"global": {
				"pool6": "64:ff9b::/96"
			}
		}
		"""

