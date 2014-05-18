from __future__ import with_statement

__plugin_name__ = "CustomWhitelist"
__plugin_version__ = "1.0"
__plugin_mainclass__ = "brix"

import os,math,re
from java.io import FileInputStream,File
from java.lang import String
from org.bukkit.util import Vector
from org.bukkit.configuration.file import YamlConfiguration
import org.bukkit as bukkit
from java.util.logging import Level
import java.util.ArrayList as ArrayList
import java.util.HashMap
import org.bukkit.block.Block
import org.bukkit.enchantments.Enchantment
import org.bukkit.Material
import org.bukkit.entity.Player
import org.bukkit.event.EventHandler
import org.bukkit.event.EventPriority
import org.bukkit.event.Listener
import org.bukkit.event.block.BlockBreakEvent
import org.bukkit.inventory.ItemStack as ItemStack
import org.bukkit.inventory.meta
import org.bukkit.event.entity.CreatureSpawnEvent
import org.bukkit.command.Command
import org.bukkit.command.CommandSender
import org.bukkit.entity.Player as player
import org.bukkit.event
import org.bukkit.event.player.PlayerInteractEvent
import org.bukkit.inventory.meta.ItemMeta
import org.bukkit.plugin.java.JavaPlugin
Material = bukkit.Material
import org.bukkit.block
import org.bukkit.entity
import org.bukkit.entity.EntityType
log = server.getLogger()
import org.bukkit.event.entity.EntityTargetEvent
from java.util import Random
import org.bukkit.event.entity.EntityDeathEvent
from random import randrange
from random import randint
import random
import java.awt.event.KeyEvent 
import warnings
import org.bukkit.event.entity.EntityDamageByEntityEvent
import org.bukkit.inventory.ShapedRecipe as ShapedRecipe
import org.bukkit.material.MaterialData as MaterialData
import org.bukkit.Bukkit
import org.bukkit.potion.PotionEffect as PotionEffect
import org.bukkit.potion.PotionEffectType as PotionEffectType
import org.bukkit.event.player.PlayerItemHeldEvent
import unicodedata
import fileinput
from itertools import ifilterfalse 
import org.bukkit.event.player.PlayerLoginEvent
import org.bukkit.event.player.PlayerPreLoginEvent


server = bukkit.Bukkit.getServer()

BLACK = org.bukkit.ChatColor.BLACK
DARK_BLUE = org.bukkit.ChatColor.DARK_BLUE
DARK_GREEN = org.bukkit.ChatColor.DARK_GREEN
DARK_AQUA = org.bukkit.ChatColor.DARK_AQUA
DARK_RED = org.bukkit.ChatColor.DARK_RED
DARK_PURPLE = org.bukkit.ChatColor.DARK_PURPLE  
GOLD = org.bukkit.ChatColor.GOLD
GRAY = org.bukkit.ChatColor.GRAY
DARK_GRAY = org.bukkit.ChatColor.DARK_GRAY
GREEN = org.bukkit.ChatColor.GREEN
AQUA = org.bukkit.ChatColor.AQUA
RED = org.bukkit.ChatColor.RED
YELLOW = org.bukkit.ChatColor.YELLOW
WHITE = org.bukkit.ChatColor.WHITE


log = server.getLogger()
CHAT_PREFIX = "[CustomWhitelist] "
def info(*text):
    log.log(Level.INFO,CHAT_PREFIX+" ".join(map(unicode,text)))
def severe(*text):
    log.log(Level.SEVERE,CHAT_PREFIX+" ".join(map(unicode,text)))
def msg(player,*text):
    player.sendMessage(CHAT_PREFIX+" ".join(map(unicode,text)))

CONSOLE = server.getConsoleSender()

class brix(PythonPlugin):
    def __init__(self):
        PythonPlugin.__init__(self)
        self.api = None
        self.cfg = None
        self.folder = ""
        self.nameChecker = re.compile("^[a-zA-Z0-9\._]+$")
        
    def onEnable(self):
        pluginlokacija1 = os.path.realpath("%s/plugins"%os.getcwd())
        if os.path.isfile("%s/CustomWhitelist/config.yml"%pluginlokacija1):
           self.findFolder()
           self.cfg = YamlConfiguration.loadConfiguration(File(os.path.join(self.folder,"config.yml")))
        else:
            os.mkdir("%s/CreativePoints/"%pluginlokacija1)
            self.findFolder()
            self.cfg = YamlConfiguration.loadConfiguration(File(os.path.join(self.folder,"config.yml")))
            
    def saveCfg(self):
        pluginlokacija1 = os.path.realpath("%s/plugins"%os.getcwd())
        if os.path.isfile("%s/CustomWhitelist/config.yml"%pluginlokacija1):
           self.findFolder()
           self.cfg = YamlConfiguration.loadConfiguration(File(os.path.join(self.folder,"config.yml")))
        else:
            os.mkdir("%s/CustomWhitelist/"%pluginlokacija1)
            self.findFolder()
            self.cfg = YamlConfiguration.loadConfiguration(File(os.path.join(self.folder,"config.yml")))
            
    #@hook.command("autoconfig", usage="/<command>", desc="Generates new config.")        
    #def createConfig(sender, command, args):
    #    if sender.hasPermission("pets.autocfg"):
    #       pluginlokacija2 = os.path.realpath("%s/plugins"%os.getcwd())
    #       fo = open("%s/ItemEffect/config.yml"%pluginlokacija2, "wb")
    #       fo.write( "main:\n  STICK:\n    effect: SPEED\n    duration: 30\n    clickable: true\n    amplifier: 1")
    #       fo.close
    #       sender.sendMessage("%sNew default config was generated successfully."%bukkit.ChatColor.DARK_AQUA)
 
    def findFolder(self):
          pluginfolder = os.path.split(self.dataFolder.toString())[0]
          for name in os.listdir(pluginfolder):
              if self.dataFolder.toString().lower() == os.path.join(pluginfolder,name).lower():
                 self.folder = os.path.join(pluginfolder,name)
                 
    def getCfg(self):
        getcfg = self.cfg
        return getcfg

    @hook.event("player.PlayerLoginEvent", "HIGH")
    def onPlayerLoginEvent(event):
        section = pyplugin.getCfg().getConfigurationSection("main")
        enabled = section.getString("enabled")
        pluginlokacija1 = os.path.realpath("%s/plugins"%os.getcwd())
        if enabled == "true":
           if not event.getPlayer().getName() in open("%s/CustomWhitelist/igraci.yml"%pluginlokacija1).read():
              poruka = section.getString("poruka")
              customstring = bukkit.ChatColor.translateAlternateColorCodes('&', poruka)
              event.disallow(org.bukkit.event.player.PlayerLoginEvent.Result.KICK_OTHER, customstring)
              print "Igrac %s je pokusao uci ali nije na CustomWhitelisti."%event.getPlayer().getName()

    @hook.command("customwhitelist", usage="/cw [args]", desc="Opsta CustomWhitelist komanda!",
                 aliases = ["cw", "customw"])
    def customwhitelist(sender, command, args):
        section = pyplugin.getCfg().getConfigurationSection("main")
        pluginlokacija1 = os.path.realpath("%s/plugins"%os.getcwd())
        textfile = open("%s/CustomWhitelist/igraci.yml"%pluginlokacija1, 'r+')
        if sender.hasPermission("cw.komande"):
           if sender.hasPermission("cw.reload"):
              if len(args) == 1:
                 if args[0] == "reload": 
                    if sender.hasPermission("cw.reload"):
                       plugin = org.bukkit.Bukkit.getServer().getPluginManager().getPlugin("CustomWhitelist")
                       YamlConfiguration.loadConfiguration(File(os.path.join("%s/CustomWhitelist/"%pluginlokacija1,"config.yml"))).load(File(os.path.join("%s/CustomWhitelist/"%pluginlokacija1,"config.yml")))
                       pyplugin.onEnable()
                       sender.sendMessage("%s[CustomWhitelist]%sConfig reloadan."%(bukkit.ChatColor.DARK_GREEN, bukkit.ChatColor.GREEN))
                 elif args[0] == "list" or args[0] == "lista":
                      if sender.hasPermission("cw.lista"):
                         lista = []
                         for line in textfile.readlines():
                             if not line.isspace():
                                lista.append(line)
                         sender.sendMessage("%sLista igraca koji su na whitelisti:"%bukkit.ChatColor.DARK_AQUA)
                         sender.sendMessage("%s%s"%(bukkit.ChatColor.AQUA, lista))
                 else:
                     sender.sendMessage("%sNepoznat argumenat. Dostupni argumenti su: reload, poruka, lista, dodaj, brisi."%bukkit.ChatColor.RED) 
              elif len(args) == 2:
                   if sender.hasPermission("cw.admin"):
                      if args[0] == "poruka":
                         section.set(message, args[1])
                         sender.sendMessage("%sWhitelist poruka promijenjena."%bukkit.ChatColor.DARK_AQUA)
                         sender.sendMessage("%sNova poruka je:"%bukkit.ChatColor.DARK_AQUA)
                         sender.sendMessage("%s%s"%(bukkit.ChatColor.DARK_AQUA, args[1]))
                      elif args[0] == "dodaj" or args[0] == "add":
                           with open("%s/CustomWhitelist/igraci.yml"%pluginlokacija1, "ab+") as fo:
                                fo.write("\n%s"%args[1])
                                sender.sendMessage("%sIgrac %s%s %sje dodan na custom whitelistu."%(bukkit.ChatColor.DARK_AQUA, bukkit.ChatColor.AQUA, args[1], bukkit.ChatColor.DARK_AQUA))
                      elif args[0] == "brisi" or args[0] == "del":
                           w = "%s"%args[1]
                           if w in open("%s/CustomWhitelist/igraci.yml"%pluginlokacija1).read():
                              a = filter(lambda x: not x.startswith(w), \
                                                          textfile.readlines())
                              textfile.seek(0)
                              textfile.truncate()
                              textfile.writelines(list(a))
                              textfile.close()
                              sender.sendMessage("%sIgrac %s%s %sje uspjesno izbrisan sa custom whiteliste."%(bukkit.ChatColor.DARK_AQUA, bukkit.ChatColor.AQUA, args[1], bukkit.ChatColor.DARK_AQUA))
                      else:
                         sender.sendMessage("%sNepoznat argumenat. Dostupni argumenti su: reload, poruka.."%bukkit.ChatColor.RED) 
                   else:
                      sender.sendMessage("%sNemas prava za mijenjanje whitelist poruke."%bukkit.ChatColor.RED)  
              else:
                  sender.sendMessage("%sPrevise argumenata! Dostupni argumenti su: reload, poruka, lista, dodaj, brisi.."%bukkit.ChatColor.RED)      
           else:
              sender.sendMessage("%sNemas prava da reloadas plugin!"%bukkit.ChatColor.RED)  
        else:
            sender.sendMessage("%sNemas prava za /cw komande!"%bukkit.ChatColor.RED)
        return True
