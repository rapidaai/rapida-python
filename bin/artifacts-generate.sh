python3 -m grpc.tools.protoc \
    -I ./rapida/clients/protos/artifacts \
    --pyi_out=./rapida/clients/protos \
    --python_out=./rapida/clients/protos \
    --grpc_python_out=./rapida/clients/protos \
    ./rapida/clients/protos/artifacts/*.proto



# for file in rapida/clients/protos/*.py; do
#     if grep -q "import assistant_.*_pb2" "$file"; then
#         sed 's/import \(assistant_.*_pb2\)/import rapida.clients.protos.\1/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
#     fi
# done
for file in rapida/clients/protos/*.py rapida/clients/protos/*.pyi; do

# import document_api_pb2 as document__api__pb2

     if grep -q "import .*_api_pb2 " "$file"; then
        sed 's/import \(.*_api_pb2\)/import rapida.clients.protos.\1/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle assistant_*_pb2 imports
    if grep -q "import assistant_.*_pb2" "$file"; then
        sed 's/import \(assistant_.*_pb2\)/import rapida.clients.protos.\1/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle common_pb2 imports
    if grep -q "import common_pb2" "$file"; then
        sed 's/import common_pb2 as common__pb2/import rapida.clients.protos.common_pb2 as common__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
        sed 's/import common_pb2 as _common_pb2/import rapida.clients.protos.common_pb2 as _common_pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle web_api_pb2 imports
    if grep -q "import web_api_pb2" "$file"; then
        sed 's/import web_api_pb2 as web__api__pb2/import rapida.clients.protos.web_api_pb2 as web__api__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle provider_api_pb2 imports
    if grep -q "import provider_api_pb2" "$file"; then
        sed 's/import provider_api_pb2 as provider__api__pb2/import rapida.clients.protos.provider_api_pb2 as provider__api__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle vault_api_pb2 imports
    if grep -q "import vault_api_pb2" "$file"; then
        sed 's/import vault_api_pb2 as vault__api__pb2/import rapida.clients.protos.vault_api_pb2 as vault__api__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle integration_api_pb2 imports
    if grep -q "import integration_api_pb2" "$file"; then
        sed 's/import integration_api_pb2 as integration__api__pb2/import rapida.clients.protos.integration_api_pb2 as integration__api__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle knowledge_api_pb2 imports
    if grep -q "import knowledge_api_pb2" "$file"; then
        sed 's/import knowledge_api_pb2 as knowledge__api__pb2/import rapida.clients.protos.knowledge_api_pb2 as knowledge__api__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle invoker_api_pb2 imports
    if grep -q "import invoker_api_pb2" "$file"; then
        sed 's/import invoker_api_pb2 as invoker__api__pb2/import rapida.clients.protos.invoker_api_pb2 as invoker__api__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle assistant_deployment_pb2 imports
    if grep -q "import assistant_deployment_pb2" "$file"; then
        sed 's/import assistant_deployment_pb2 as assistant__deployment__pb2/import rapida.clients.protos.assistant_deployment_pb2 as assistant__deployment__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi

    # Handle talk_api_pb2 imports
    if grep -q "import talk_api_pb2" "$file"; then
        sed 's/import talk_api_pb2 as talk__api__pb2/import rapida.clients.protos.talk_api_pb2 as talk__api__pb2/g' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi
done

# Remove backup files created by sed
find "rapida/clients/protos/" -name '*.bak' -exec rm {} +
