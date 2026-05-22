"""
Quick diagnostic script to test Supabase connection.
Run this directly: python test_supabase.py
"""
import urllib.request
import json

SUPABASE_URL = "https://kbvcesajbrjaypgrlvlj.supabase.co"
SUPABASE_KEY = "sb_publishable_232W2axkG3DEESGNCgchog_3ZBkrL3g"

print("=" * 60)
print("SUPABASE DIAGNOSTICS")
print("=" * 60)

# Step 1: Can we even reach the Supabase URL?
print("\n--- Step 1: Testing if Supabase URL is reachable ---")
try:
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        }
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        print(f"✅ URL is reachable! Status: {resp.status}")
except urllib.error.HTTPError as e:
    print(f"⚠️ URL responded with HTTP {e.code}: {e.reason}")
    if e.code == 401:
        print("   → API key might be wrong. Check your SUPABASE_KEY.")
    body = e.read().decode()
    print(f"   → Response body: {body[:300]}")
except urllib.error.URLError as e:
    print(f"❌ Cannot reach URL: {e.reason}")
    print("   → Possible causes:")
    print("     1. Your Supabase project is PAUSED (free tier pauses after inactivity)")
    print("     2. Wrong project URL in secrets.toml")
    print("     3. Network/firewall blocking the connection")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# Step 2: Try a simple REST call
print("\n--- Step 2: Testing SELECT on 'teachers' table ---")
try:
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/teachers?select=*",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        }
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
        print(f"✅ SELECT succeeded! Rows: {len(data)}")
        print(f"   Data: {data}")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"❌ SELECT failed (HTTP {e.code}): {body[:300]}")
except urllib.error.URLError as e:
    print(f"❌ Connection failed: {e.reason}")
except Exception as e:
    print(f"❌ Error: {e}")

# Step 3: Try INSERT
print("\n--- Step 3: Testing INSERT on 'teachers' table ---")
try:
    test_data = json.dumps({"username": "__test__", "password": "test", "name": "Test"}).encode()
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/teachers",
        data=test_data,
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        result = json.loads(resp.read().decode())
        print(f"✅ INSERT succeeded! Response: {result}")
        # Cleanup
        try:
            dreq = urllib.request.Request(
                f"{SUPABASE_URL}/rest/v1/teachers?username=eq.__test__",
                headers={
                    "apikey": SUPABASE_KEY,
                    "Authorization": f"Bearer {SUPABASE_KEY}",
                },
                method="DELETE"
            )
            urllib.request.urlopen(dreq, timeout=10)
            print("   (Test row cleaned up)")
        except:
            print("   ⚠️ Could not clean up test row")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"❌ INSERT failed (HTTP {e.code}): {body[:500]}")
    if "security" in body.lower() or "policy" in body.lower() or "RLS" in body:
        print("\n   → RLS is blocking the insert!")
        print("   → Fix: Disable RLS or add policies (see below)")
except urllib.error.URLError as e:
    print(f"❌ Connection failed: {e.reason}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 60)
print("WHAT TO CHECK")
print("=" * 60)
print("""
If you see 'Cannot reach URL' or 'Connection failed':

  1. CHECK IF PROJECT IS PAUSED:
     → Go to https://supabase.com/dashboard
     → If your project shows 'Paused', click 'Restore'
     → Free-tier projects pause after 7 days of inactivity!

  2. VERIFY YOUR URL:
     → Go to Supabase Dashboard → Settings → API
     → Copy the 'Project URL' and paste it in .streamlit/secrets.toml

  3. VERIFY YOUR API KEY:
     → Go to Supabase Dashboard → Settings → API 
     → Copy the 'anon public' key (or publishable key)
     → Paste it as SUPABASE_KEY in .streamlit/secrets.toml

If you see RLS errors on INSERT:
  → Go to Table Editor → teachers → disable RLS for now
""")
