import { log } from 'console';
import * as path from 'path';
import * as vscode from 'vscode';
import {
    LanguageClient,
    LanguageClientOptions,
    Message,
    ServerOptions,
    ShowMessageNotification,
    TransportKind,
} from 'vscode-languageclient/node';

let client: LanguageClient;

export function activate(context: vscode.ExtensionContext) {
    // Server options: run the LSP server
    const serverModule = context.asAbsolutePath(
        path.join('..','..', 'src', 'main.py') // Adjust the path to your server script
    );
    const serverOptions: ServerOptions = {
        command: context.asAbsolutePath(path.join('..','..', 'venv', 'Scripts', 'python.exe')),
        args: [serverModule],
        transport: TransportKind.stdio,
    };

    // Client options
    const clientOptions: LanguageClientOptions = {
        documentSelector: [{ scheme: 'file', language: 'hardscript' }], // Adjust the language as needed
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/*.hard'), // Adjust file types
        },
    };

    // Create and start the Language Client
    client = new LanguageClient(
			'hardscriptLanguageServer',
			'HardScript Language Server',
			serverOptions,
			clientOptions
    );
    client.start();
		vscode.window.showInformationMessage('HardScript Language Server started');
}

export function deactivate(): Thenable<void> | undefined {
    return client ? client.stop() : undefined;
}
